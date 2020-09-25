import os
import cv2
import numpy as np
import face_recognition as fr
from PIL import Image
from Cartoonization import test

def make_image(user_id):
    # 1. 이미지 받기
    original_image_path = "./images/input_images/HYJ.jpg"
    original_image_name = original_image_path[22:-4]
    origin_image = cv2.imread(original_image_path, cv2.IMREAD_UNCHANGED)
    BGRA_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2BGRA)

    # 1-1. 얼굴 정렬 / face_alignment


    # 2-1. Face Recognition으로 Nukki에 쓸 좌표 구하기
    fr_image = fr.load_image_file(original_image_path)
    fr_landmarks_list = fr.face_landmarks(fr_image)
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
    image = BGRA_image
    mask = np.zeros(image.shape, dtype=np.uint8)
    roi_corners = np.array([nukki_coordinate], dtype=np.int32)

    channel_count = image.shape[2]
    ignore_mask_color = (255, ) * channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)

    Nukkied_image = cv2.bitwise_and(image, mask)

    Trim_x, Trim_y = (int(chin_start[0]), int(
        chin_end[0])), (int(min_y), int(fr_chin_bottom))
    Trimmed_image = Nukkied_image[Trim_y[0]: Trim_y[1], Trim_x[0]: Trim_x[1]]

    Nukkied_image = cv2.resize(Trimmed_image, (175, 210),
                            fx=1, fy=1, interpolation=cv2.INTER_AREA)

    Nukkied_image_path = './images/nukkied_images'
    cv2.imwrite(os.path.join(Nukkied_image_path,
                            'Nukkied_' + original_image_name + '.png'), Nukkied_image)


    # 2-3. Cartoonization 이미지 변환
    target_image = 'Nukkied_' + original_image_name + '.png'
    cartooned_image_name = test.cartoonize(Nukkied_image_path, target_image)
    cartooned_image_path = './images/cartooned_images/' + cartooned_image_name


    # 2-3-1. resize
    cartooned_image = Image.open(cartooned_image_path)
    cartooned_RGBA_image = cartooned_image.convert('RGBA')
    cartooned_RGBA_image = cartooned_RGBA_image.resize((175, 210), resample=3,
                                                    box=None, reducing_gap=None)
    resized_cartooned_path = './images/cartooned_images/' + 'resized_' + cartooned_image_name
    cartooned_RGBA_image.save(resized_cartooned_path, 'PNG')


    # 2-4. re-Nukki
    fr_image = fr.load_image_file(resized_cartooned_path)
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


    image = cv2.imread(resized_cartooned_path, cv2.IMREAD_UNCHANGED)

    mask = np.zeros(image.shape, dtype=np.uint8)
    roi_corners = np.array([nukki_coordinate], dtype=np.int32)

    channel_count = image.shape[2]
    ignore_mask_color = (255, ) * channel_count
    cv2.fillPoly(mask, roi_corners, ignore_mask_color)

    re_Nukkied_image = cv2.bitwise_and(image, mask)

    re_Nukkied_image_path = os.path.join('./images/re_nukkied_images',
                            're_Nukkied_' + original_image_name + '.png')
    cv2.imwrite(re_Nukkied_image_path, re_Nukkied_image)


    # 3. 몸에 합성
    baby_face = cv2.imread(re_Nukkied_image_path, cv2.IMREAD_UNCHANGED)
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