import cv2
import os
import face_recognition
from PIL import Image, ImageDraw
# from IPython.display import Image, display
from matplotlib import pyplot

image = face_recognition.load_image_file(
    "AIrang/images/family2.jpg")
face_locations = face_recognition.face_locations(image)
face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')
    # 이미지 색칠


# pil_image.show()

# 얼굴인식 확인
# for (top, right, bottom, left) in face_locations:
#     cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 1)

# pyplot.rcParams["figure.figsize"] = (16, 16)
# pyplot.imshow(image)
pyplot.imshow(pil_image)
pyplot.show()
