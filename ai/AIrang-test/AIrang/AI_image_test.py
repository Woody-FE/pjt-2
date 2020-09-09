import cv2
import os
import face_recognition
from IPython.display import Image, display
from matplotlib import pyplot

family_image_path = "./images/family1.jpg"
tale_image_path = "./images/ariel.jpg"

family_image = face_recognition.load_image_file(family_image_path)
tale_image = face_recognition.load_image_file(tale_image_path)

family_face_locations = face_recognition.face_locations(family_image)
tale_face_locations = face_recognition.face_locations(tale_image)

list_of_family_face_encodings = face_recognition.face_encodings(family_image)
list_of_tale_face_encodings = face_recognition.face_encodings(tale_image)

for (top, right, bottom, left) in family_face_locations:
    cv2.rectangle(family_image, (left, top), (right, bottom), (0, 255, 0), 3)

# pyplot.rcParams["figure.figsize"] = (16, 16)
# pyplot.imshow(family_image)
# pyplot.show()

# 이미지 list 확인
# for face in family_face
