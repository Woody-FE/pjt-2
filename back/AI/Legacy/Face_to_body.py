import cv2
import numpy as np
import face_recognition as fr

baby_face = cv2.imread('./Resized_image.png', cv2.IMREAD_UNCHANGED)
baby_body = cv2.imread('./images/Remove_white_body.png', cv2.IMREAD_UNCHANGED)
baby_hat = cv2.imread('./images/Remove_white_hat.png', cv2.IMREAD_UNCHANGED)

component = [baby_face, baby_body, baby_hat]
for i in range(3):
    if component[i].shape[2] != 4:
        # -1 loads as-is so if it will be 3 or 4 channel as the original
        BGRA_img = cv2.cvtColor(component[i], cv2.COLOR_BGR2BGRA)
        component[i] = BGRA_img
baby_face, baby_body, baby_hat = component[0], component[1], component[2]

# baby_hat image resize
Resized_image = cv2.resize(baby_hat, (300, 200), fx=1,
                           fy=1, interpolation=cv2.INTER_AREA)
baby_hat = Resized_image

# print('baby_face', baby_face.shape)
# print('baby_body', baby_body.shape)
# print('baby_hat', baby_hat.shape)

# 몸 얼굴 정렬
face_body_tilt = (-10, 92)
face_hat_tilt = (-10, 0)

# Image Addtion with Alpha

# 1. face + body
x_offset, y_offset = int(
    0.5 * baby_body.shape[1] - 0.5 * baby_face.shape[1] + face_body_tilt[0]), face_body_tilt[1]
for c in range(0, 3):
    baby_body[y_offset:y_offset+baby_face.shape[0], x_offset:x_offset+baby_face.shape[1], c] = baby_face[:, :, c] * \
        (baby_face[:, :, 3]/255.0) + baby_body[y_offset:y_offset+baby_face.shape[0],
                                               x_offset:x_offset + baby_face.shape[1], c] * (1.0 - baby_face[:, :, 3]/255.0)
baby_face_body = baby_body.copy()

# 2. + hat
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

cv2.waitKey(0)
cv2.destroyAllWindows()

# 1. 턱 끝, 머리 양 쪽 좌표
# 2. 옷 기준 좌표
