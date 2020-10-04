import os
import cv2
import math
import numpy as np
import face_recognition as fr
from PIL import Image
from .Cartoonization import test

from django.conf import settings


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

    
    # test..
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

    fr_left_eyebrow = fr_landmarks_list[0]['left_eyebrow']
    fr_right_eyebrow = fr_landmarks_list[0]['right_eyebrow']

    eyebrow_y = np.max(np.array(fr_left_eyebrow + fr_left_eyebrow), axis = 0)[1]

    np_fr_chin = np.array(fr_chin)
    fr_chin_bottom = np.max(np_fr_chin)

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
    re_Nukkied_RGBA_Image = cv2.cvtColor(re_Nukkied_image, cv2.COLOR_BGR2RGBA)

    re_Nukkied_PIL_RGBA_image = Image.fromarray(re_Nukkied_RGBA_Image)

    datas = re_Nukkied_PIL_RGBA_image.getdata()
    
    newData = []
    cutOff = 0

    for item in datas:
        if item[0] <= cutOff and item[1] <= cutOff and item[2] <= cutOff:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    re_Nukkied_PIL_RGBA_image.putdata(newData)


    # 3. 합성
    baby_face_BGRA = np.array(re_Nukkied_PIL_RGBA_image)
    baby_face = cv2.cvtColor(baby_face_BGRA, cv2.COLOR_BGRA2RGBA)

    
    # 3-1. 모자 이미지 파일들 불러오기
    hat_images_path = f'{settings.BASE_DIR}/accounts/image_to_cartoon/images/hat_images'
    # 20200928 서버에 올렸을 때 다른 모자가 불러와져서 하드코딩으로 모자 입력함(임창묵)
    hat_image_files = [f for f in os.listdir(hat_images_path) if os.path.isfile(os.path.join(hat_images_path, f))]
    kindergarden_hat_path = hat_images_path + '/kindergarden_hat.png'
    magician_hat_path = hat_images_path + '/magician_hat.png'
    musician_hat_path = hat_images_path + '/musician_hat.png'
    police_hat_path = hat_images_path + '/police_hat.png'
    singer_hat_path = hat_images_path + '/singer_hat.png'
    zookeeper_hat_path = hat_images_path + '/zookeeper_hat.png'


    hat_images = np.empty(len(hat_image_files), dtype = object)
    hat_images[0] = cv2.imread(kindergarden_hat_path, cv2.IMREAD_UNCHANGED)
    hat_images[1] = cv2.imread(magician_hat_path, cv2.IMREAD_UNCHANGED)
    hat_images[2] = cv2.imread(musician_hat_path, cv2.IMREAD_UNCHANGED)
    hat_images[3] = cv2.imread(police_hat_path, cv2.IMREAD_UNCHANGED)
    hat_images[4] = cv2.imread(singer_hat_path, cv2.IMREAD_UNCHANGED)
    hat_images[5] = cv2.imread(zookeeper_hat_path, cv2.IMREAD_UNCHANGED)


    # 결과 모아놓을 numpy array
    result_image_array = np.empty(len(hat_image_files), dtype = object)


    # 모자만 합성
    for i in range(len(hat_image_files)):

        # kindergarden_hat = hat_images[0]
        # magician_hat = hat_images[1]
        # musician_hat = hat_images[2]
        # police_hat = hat_images[3]
        # singer_hat = hat_images[4]
        # zookeeper_hat = hat_images[5]
        baby_hat = hat_images[i]


        # 3-1-2.tilt
        face_canvas_tilt = (int(baby_hat.shape[0]), 3)
        if i == 4:
            hat_canvas_tilt = (eyebrow_y + 15, 0)
        else:
            hat_canvas_tilt = (eyebrow_y, 0)


        # 3-2. make canvas
        canvas_size = (baby_face.shape[0] + baby_hat.shape[0], max(baby_face.shape[1], baby_hat.shape[1]))
        canvas_hat_image = np.zeros((canvas_size[0], canvas_size[1], 4), dtype=np.uint8)
        canvas_face_image = np.zeros((canvas_size[0], canvas_size[1], 4), dtype=np.uint8)


        # 3-2-1. hat on canvas
        x_offset, y_offset = int((canvas_hat_image.shape[1] - baby_hat.shape[1])/2), hat_canvas_tilt[0]
        canvas_hat_image[y_offset:y_offset + baby_hat.shape[0],
        x_offset:x_offset + baby_hat.shape[1], :baby_hat.shape[2]] = baby_hat
        

        # 3-2-2. face on canvas
        x_offset, y_offset = int((canvas_face_image.shape[1] - baby_face.shape[1])/2) + face_canvas_tilt[1], face_canvas_tilt[0]
        canvas_face_image[y_offset:y_offset + baby_face.shape[0],
        x_offset:x_offset + baby_face.shape[1], :baby_face.shape[2]] = baby_face

        
        # 3-3. 겹치는 부분은 모자만
        PIL_face_image = Image.fromarray(canvas_face_image)
        PIL_hat_image = Image.fromarray(canvas_hat_image)
        PIL_face_image.paste(PIL_hat_image, (0, 0), PIL_hat_image)

        result_image_array[i] = np.array(PIL_face_image)


    # 4. 결과 출력
    store_path = f'{settings.BASE_DIR}/images/user/{user_id}/conversion/'

    for i in range(len(result_image_array)):
        cv2.imwrite(f'{store_path}{i}.png', result_image_array[i])

    return store_path


def show_me_hat_and_face(input_image_path, user_id, hat_idx = 0):
    store_path = f'{settings.BASE_DIR}/images/user/{user_id}/conversion/'
    hat_and_face_folder_path = f'{settings.BASE_DIR}/images/user/{user_id}/conversion/'
    hat_and_face_image_path = f'{hat_and_face_folder_path}{hat_idx}.png'
    hat_and_face_image_name = hat_and_face_image_path.split('conversion/')[1]

    if not os.path.isdir(store_path):
        os.makedirs(store_path)


    # if not os.path.isfile(hat_and_face_image_path):
        # print('FILENAME: ' + '" ' + hat_and_face_image_name + ' "' + ' dose not exist... :(')
    hat_and_face(input_image_path, user_id)
    return hat_and_face_image_path

    # else:
    #     # print('FILENAME: ' + '" ' + hat_and_face_image_name + ' "' + ' exist! :)')
    #     return hat_and_face_image_path