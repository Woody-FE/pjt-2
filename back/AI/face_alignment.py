import os
import cv2
import numpy as np
import face_recognition as fr
from PIL import Image
from Cartoonization import test
import math

original_image_path = './images/input_images/rotate_right.jpg'
origin_image = cv2.imread(original_image_path, cv2.IMREAD_UNCHANGED)
BGRA_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2BGRA)

# 1-1. 얼굴 정렬 / face_alignment
fr_image = fr.load_image_file(original_image_path)
fr_landmarks_list = fr.face_landmarks(fr_image)
fr_left_eye= fr_landmarks_list[0]['left_eye']
fr_right_eye= fr_landmarks_list[0]['right_eye']
np_left_eye, np_right_eye = np.array(fr_left_eye), np.array(fr_right_eye)
left_eye_sum, right_eye_sum = np_left_eye.sum(axis=0), np_right_eye.sum(axis=0)
left_eye_center = (round(left_eye_sum[0]/len(np_left_eye), 2), round(left_eye_sum[1]/len(np_left_eye), 2))
right_eye_center = (round(right_eye_sum[0]/len(np_right_eye), 2), round(right_eye_sum[1]/len(np_right_eye), 2))
print(left_eye_center, right_eye_center)

left_eye_x = left_eye_center[0]; left_eye_y = left_eye_center[1]
right_eye_x = right_eye_center[0]; right_eye_y = right_eye_center[1]


if left_eye_y < right_eye_y:
   point_3rd = (right_eye_x, left_eye_y)
   direction = -1 #rotate same direction to clock
   print("rotate to clock direction")
else:
   point_3rd = (left_eye_x, right_eye_y)
   direction = 1 #rotate inverse direction of clock
   print("rotate to inverse clock direction")

def euclidean_distance(a, b):
    x1 = a[0]; y1 = a[1]
    x2 = b[0]; y2 = b[1]
    return math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))

a = euclidean_distance(left_eye_center, point_3rd)
b = euclidean_distance(right_eye_center, left_eye_center)
c = euclidean_distance(right_eye_center, point_3rd)

cos_a = (b*b + c*c - a*a)/(2*b*c)
print("cos(a) = ", cos_a)
 
angle = np.arccos(cos_a)
print("angle: ", angle," in radian")
 
angle = (angle * 180) / math.pi
print("angle: ", angle," in degree")


if direction == -1:
   angle = 90 - angle

angle = (-1) * angle

new_image = Image.fromarray(BGRA_image)

rotated_image= np.array(new_image.rotate(direction * angle))

red, green, blue, alpha= rotated_image.T 
rotated_image = np.array([blue, green, red, alpha])
rotated_image = rotated_image.transpose()

rotated_image = Image.fromarray(rotated_image)

rotated_image.save('rotated_img.png')

