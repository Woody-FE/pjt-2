import cv2
import numpy as np
import face_recognition as fr
from Cartoonization import test as Cartoonization


# 1. 이미지 받기
original_image_path = "./images/input_images/KTI.jpg"
original_image_name = original_image_path[22:]
# print(original_image_name)
origin_img = cv2.imread(original_image_path, cv2.IMREAD_UNCHANGED)
BGRA_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2BGRA)


# 2-1. Face Recognition으로 Nukki에 쓸 좌표 구하기
fr_image = fr.load_image_file(original_image_path)
fr_landmarks_list = fr.face_landmarks(fr_image)
fr_chin = fr_landmarks_list[0]['chin']

np_fr_chin = np.array(fr_chin)
fr_chin_bottom = np.max(np_fr_chin, axis=0)[1]

chin_x, chin_y = np_fr_chin[np.argmax(chin_y)], np_fr_chin[:, 1:]
chin_start, chin_end = np_fr_chin[0], np_fr_chin[-1]

upper_head = []
L = len(np_fr_chin)
for i in range(L-1, -1, -1):
    if i < L % 2:
        temp = (np_fr_chin[i][0], 0.85 * (chin_start[1] -
                                          (np_fr_chin[i][1] - chin_start[1])))
    else:
        temp = (np_fr_chin[i][0], 0.85 *
                (chin_end[1] - (np_fr_chin[i][1] - chin_end[1])))
    upper_head.append(temp)

fr_left_eyebrow = fr_landmarks_list[0]['left_eyebrow']
fr_right_eyebrow = fr_landmarks_list[0]['right_eyebrow']

bump = 0.05 * (chin_end[0] - chin_start[0])

min_y = 0.8 * min(np.min(fr_left_eyebrow, axis=0)
                  [1], np.min(fr_right_eyebrow, axis=0)[1])
eyelash_left_start, eyelash_right_end = (
    chin_start[0] + bump, min_y), (chin_end[0] - bump, min_y)

nukki_coordinate = []
nukki_coordinate.append(eyelash_left_start)
nukki_coordinate.extend(fr_chin)
nukki_coordinate.append(eyelash_right_end)


# 2-2. 얼굴 이미지 자르기
image = BGRA_img
mask = np.zeros(image.shape, dtype=np.uint8)
roi_corners = np.array([nukki_coordinate], dtype=np.int32)

channel_count = image.shape[2]
ignore_mask_color = (255, ) * channel_count
cv2.fillPoly(mask, roi_corners, ignore_mask_color)

Nukkied_image = cv2.bitwise_and(image, mask)

Trim_x, Trim_y = (int(chin_start[0]), int(
    chin_end[0])), (int(min_y), int(fr_chin_bottom))
Trimmed_image = Nukkied_image[Trim_y[0]: Trim_y[1], Trim_x[0]: Trim_x[1]]

Resized_image = cv2.resize(Trimmed_image, (180, 200),
                           fx=1, fy=1, interpolation=cv2.INTER_AREA)

# cv2.imwrite('Nukkied_image.png', Nukkied_image)
# cv2.imwrite('Trimmed_image.png', Trimmed_image)
cv2.imwrite('Resized_image.png', Resized_image)


# 2-3. Cartoonization 이미지 변환
Cartoonization()


# 3. 몸에 합성
baby_face = cv2.imread('./Resized_image.png', cv2.IMREAD_UNCHANGED)
baby_body = cv2.imread('./images/Remove_white_body.png', cv2.IMREAD_UNCHANGED)
baby_hat = cv2.imread('./images/Remove_white_hat.png', cv2.IMREAD_UNCHANGED)

component = [baby_face, baby_body, baby_hat]
for i in range(3):
    if component[i].shape[2] != 4:
        # -1 loads as-is so if it will be 3 or 4 channel as the original
        BGRA_img = cv2.cvtColor(component[i], cv2.COLOR_BGR2BGRA)
        component[i] = BGRA_img

# baby_hat image resize
component[2] = cv2.resize(baby_hat, (300, 200), fx=1,
                          fy=1, interpolation=cv2.INTER_AREA)

baby_face, baby_body, baby_hat = component[0], component[1], component[2]

# print('baby_face', baby_face.shape)
# print('baby_body', baby_body.shape)
# print('baby_hat', baby_hat.shape)

# tilt
face_body_tilt = (-10, 92)
face_hat_tilt = (-10, 0)

# +body
x_offset, y_offset = int(
    0.5 * baby_body.shape[1] - 0.5 * baby_face.shape[1] + face_body_tilt[0]), face_body_tilt[1]
for c in range(0, 3):
    baby_body[y_offset:y_offset+baby_face.shape[0], x_offset:x_offset+baby_face.shape[1], c] = baby_face[:, :, c] * \
        (baby_face[:, :, 3]/255.0) + baby_body[y_offset:y_offset+baby_face.shape[0],
                                               x_offset:x_offset + baby_face.shape[1], c] * (1.0 - baby_face[:, :, 3]/255.0)
baby_face_body = baby_body.copy()

# +hat
x_offset, y_offset = int(
    0.5 * baby_face_body.shape[1] - 0.5 * baby_hat.shape[1] + face_hat_tilt[0]), face_hat_tilt[1]
for c in range(0, 3):
    baby_face_body[y_offset:y_offset+baby_hat.shape[0], x_offset:x_offset+baby_hat.shape[1], c] = baby_hat[:, :, c] * \
        (baby_hat[:, :, 3]/255.0) + baby_face_body[y_offset:y_offset+baby_hat.shape[0],
                                                   x_offset:x_offset + baby_hat.shape[1], c] * (1.0 - baby_hat[:, :, 3]/255.0)

# Result
result = baby_face_body.copy()

cv2.imshow('Face_to_body', result)
cv2.imwrite('result.png', result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
