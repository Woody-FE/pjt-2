import cv2
import face_recognition as fr
import numpy as np

img_path = "./AIrang/images/hyj.png"

origin_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
BGRA_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2BGRA)

max_x, max_y = BGRA_img.shape[0], BGRA_img.shape[1]
# print(max_x, max_y)

# Load the jpg file into a numpy array
fr_img = fr.load_image_file(img_path)

# Find all facial features in all the faces in the image
fr_landmarks_list = fr.face_landmarks(fr_img)
fr_chin = fr_landmarks_list[0]['chin']
np_fr_chin = np.array(fr_chin)
fr_chin_bottom = np.min(np_fr_chin, axis=0)[1]
# print(np_fr_chin)
# print(fr_chin_bottom)

chin_y = np_fr_chin[:, 1:]
min_chin_idx = np.argmax(chin_y)
chin_x = np_fr_chin[min_chin_idx]
# print(np_fr_chin[min_chin_idx])

# for px in np_fr_chin:
#     print(BGRA_img[px[0]][px[1]])
#     BGRA_img[px[0]][px[1]][3] = 0

# for px in np_fr_chin:
#     print(BGRA_img[px[0]][px[1]])

for x in range(100):
    BGRA_img[x][1] = 0

Nukkied_img = BGRA_img


cv2.imshow('Origin_img', origin_img)
cv2.imshow('Nukkied_img', Nukkied_img)

# for pixel in BGRA_img:
#     print(pixel)

# # Load the jpg file into a numpy array
# fr_img = fr.load_image_file(img_path)

# # Find all facial features in all the faces in the image
# fr_landmarks_list = fr.face_landmarks(fr_img)
# fr_chin = fr_landmarks_list[0]['chin']
# np_fr_chin = np.array(fr_chin)
# fr_chin_bottom = np.min(np_fr_chin, axis=0)[1]
# # print(np_fr_chin)
# # print(fr_chin_bottom)
# chin_y_axis = np_fr_chin[:, 1:]
# min_chin_idx = np.argmax(chin_y_axis)
# # print(np_fr_chin[min_chin_idx])

# cv2.imwrite("nukkied_face.png", nukkied_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
