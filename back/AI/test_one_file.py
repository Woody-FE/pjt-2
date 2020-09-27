import os
import cv2
import math
import numpy as np
import face_recognition as fr
from PIL import Image
from Cartoonization import test


def euclidean_distance(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))


def hat_and_face(input_image_path, user_id):
    # 1. 이미지 받기
    original_image_path = input_image_path
    original_image_name = original_image_path[22:-4]
    origin_image = cv2.imread(original_image_path, cv2.IMREAD_UNCHANGED)


    # 1-1. 얼굴 정렬 / face_alignment
    fr_image = fr.load_image_file(original_image_path)
    fr_landmarks_list = fr.face_landmarks(fr_image)

    fr_left_eye, fr_right_eye= fr_landmarks_list[0]['left_eye'], fr_landmarks_list[0]['right_eye']
    np_left_eye, np_right_eye = np.array(fr_left_eye), np.array(fr_right_eye)
    left_eye_sum, right_eye_sum = np_left_eye.sum(axis=0), np_right_eye.sum(axis=0)
    left_eye_center = (round(left_eye_sum[0]/len(np_left_eye), 2), round(left_eye_sum[1]/len(np_left_eye), 2))
    right_eye_center = (round(right_eye_sum[0]/len(np_right_eye), 2), round(right_eye_sum[1]/len(np_right_eye), 2))

    left_eye_x, left_eye_y = left_eye_center
    right_eye_x, right_eye_y = right_eye_center

    if left_eye_y < right_eye_y:
        point_3rd = (right_eye_x, left_eye_y)
        # 시계방향 회전
        direction = -1
    else:
        point_3rd = (left_eye_x, right_eye_y)
        # 시계반대방향 회전
        direction = 1
    
    a = euclidean_distance(left_eye_center, point_3rd)
    b = euclidean_distance(right_eye_center, left_eye_center)
    c = euclidean_distance(right_eye_center, point_3rd)

    cos_a = (b*b + c*c - a*a)/(2*b*c)
    angle = np.arccos(cos_a)
    angle = (angle * 180) / math.pi

    if direction == -1:
        angle = 90 - angle

    angle = (-1) * angle

    input_image = Image.fromarray(origin_image)
    np_rotated_image = np.array(input_image.rotate(direction * angle))


    # 2-1. 정렬 후 Face Recognition으로 Nukki에 쓸 좌표 구하기
    fr_landmarks_list = fr.face_landmarks(np_rotated_image)
    
    fr_chin = fr_landmarks_list[0]['chin']
    np_fr_chin = np.array(fr_chin)
    fr_chin_bottom = np.max(np_fr_chin, axis=0)[1]

    chin_y = np_fr_chin[:, 1:]
    chin_x = np_fr_chin[np.argmax(chin_y)]
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
    image = np_rotated_image
    mask = np.zeros(image.shape, dtype=np.uint8)
    roi_corners = np.array([nukki_coordinate], dtype=np.int32)

    channel_count = image.shape[2]
    ignore_mask_color = (255, ) * channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)

    Nukkied_image = cv2.bitwise_and(image, mask)

    Trim_x, Trim_y = (int(chin_start[0]), int(
        chin_end[0])), (int(min_y), int(fr_chin_bottom))
    np_Trimmed_image = Nukkied_image[Trim_y[0]: Trim_y[1], Trim_x[0]: Trim_x[1]]


    # 2-3. Cartoonization 이미지 변환
    Cartooned_image = test.cartoonize(original_image_name, np_Trimmed_image)


    # 2-3-1. resize
    resize_size = (175, 210)
    Resized_cartooned_image = Cartooned_image.resize(resize_size, resample=3, box=None, reducing_gap=None)

    Trimmed_image = Image.fromarray(np_Trimmed_image)
    Resized_trimmed_image = Trimmed_image.resize(resize_size, resample=3, box=None, reducing_gap=None)


    # 2-4. re-Nukki
    fr_image = np.array(Resized_trimmed_image)
    fr_landmarks_list = fr.face_landmarks(fr_image)
    fr_chin = fr_landmarks_list[0]['chin']

    np_fr_chin = np.array(fr_chin)
    fr_chin_bottom = np.max(np_fr_chin, axis=0)[1]

    chin_y = np_fr_chin[:, 1:]
    chin_x = np_fr_chin[np.argmax(chin_y)]
    chin_start, chin_end = np_fr_chin[0], np_fr_chin[-1]

    left_start, right_end = (0, 0), (210, 0)

    nukki_coordinate = []
    nukki_coordinate.append(left_start)
    nukki_coordinate.extend(fr_chin)
    nukki_coordinate.append(right_end)


    image = np.array(Resized_cartooned_image)

    mask = np.zeros(image.shape, dtype=np.uint8)
    roi_corners = np.array([nukki_coordinate], dtype=np.int32)

    channel_count = image.shape[2]
    ignore_mask_color = (255, ) * channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)

    re_Nukkied_image = cv2.bitwise_and(image, mask)
    

    # 3. 몸에 합성
    baby_face = re_Nukkied_image
    baby_body = cv2.imread(
        './images/body_and_hat/white_removed_body.png', cv2.IMREAD_UNCHANGED)
    baby_hat = cv2.imread(
        './images/body_and_hat/white_removed_hat.png', cv2.IMREAD_UNCHANGED)


    # # 3-1.tilt
    face_body_tilt = (-8, 120)
    face_hat_tilt = (-8, 20)


    # 3-2-1. +body
    x_offset, y_offset = int(
        0.5 * baby_body.shape[1] - 0.5 * baby_face.shape[1] + face_body_tilt[0]), face_body_tilt[1]

    for c in range(0, 3):
        baby_body[y_offset:y_offset+baby_face.shape[0], x_offset:x_offset+baby_face.shape[1], c] = baby_face[:, :, c] * \
            (baby_face[:, :, 3]/255.0) + baby_body[y_offset:y_offset+baby_face.shape[0],
                                                x_offset:x_offset + baby_face.shape[1], c] * (1.0 - baby_face[:, :, 3]/255.0)


    # 3-2-2. +hat
    x_offset, y_offset = int(
        0.5 * baby_body.shape[1] - 0.5 * baby_hat.shape[1] + face_hat_tilt[0]), face_hat_tilt[1]

    for c in range(0, 3):
        baby_body[y_offset:y_offset+baby_hat.shape[0], x_offset:x_offset+baby_hat.shape[1], c] = baby_hat[:, :, c] * \
            (baby_hat[:, :, 3]/255.0) + baby_body[y_offset:y_offset+baby_hat.shape[0],
                                                x_offset:x_offset + baby_hat.shape[1], c] * (1.0 - baby_hat[:, :, 3]/255.0)

    # 4. 결과 출력

    Trim_y = (0, int(fr_chin_bottom) + 120)
    Trimmed_image = baby_body[Trim_y[0]: Trim_y[1], :]

    Trimmed_path = os.path.join('./images/my_image/' , 'baby_' + str(user_id) + '.jpg')
    cv2.imwrite(Trimmed_path, Trimmed_image)

    result_path = os.path.join('./images/my_image/' , 'baby_' + str(user_id) + '.png')

    result_image = Image.open(Trimmed_path)
    result_image = result_image.convert('RGBA')
    datas = result_image.getdata()

    newData = []
    cutOff = 10

    for item in datas:
        if item[0] <= cutOff and item[1] <= cutOff and item[2] <= cutOff:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    result_image.putdata(newData)
    result_image.save(result_path, "PNG")


    return result_path