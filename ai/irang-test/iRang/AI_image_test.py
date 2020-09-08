import cv2
import os
import face_recognition
from IPython.display import Image, display
from matplotlib import pyplot

family_image_path = "./images/family.jpg"
tale_image_path = "./images/ariel.jpg"

family_image = face_recognition.load_image_file(family_image_path)
tale_image = face_recognition.load_image_file(tale_image_path)

family_face_locations = face_recognition.face_locations(family_image)
tale_face_locations = face_recognition.face_locations(tale_image)

list_of_family_face_encodings = face_recognition.face_encodings(family_image)
list_of_tale_face_encodings = face_recognition.face_encodings(tale_image)

# print(list_of_family_face_encodings)
# print(list_of_tale_face_encoding)


# for (top, right, bottom, left) in face_locations:
#   cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)


# # 이미지 버퍼 출력
# pyplot.rcParams["figure.figsize"] = (16, 16)
# pyplot.imshow(image)
# pyplot.show()

# pyplot.rcParams["figure.figsize"] = (1, 1)


# known_image_list = []
# known_image_path = image_path
# for i in range(1, 5):
#   known_image_list.append(face_recognition.load_image_file(
#       known_image_path + "p" + str(i) + ".jpg"))


# known_face_list = []
# for person in known_image_list:
#   top, right, bottom, left = face_recognition.face_locations(person)[0]
#   face_image = person[top:bottom, left:right]
#   known_face_list.append(face_image)

# # known_face_list 이미지 저장 확인
# for face in known_face_list:
#   pyplot.imshow(face)
#   pyplot.show()

#   unknown_person = face_recognition.load_image_file(
#       known_image_path + "son.jpg")

# top, right, bottom, left = face_recognition.face_locations(unknown_person)[0]
# unknown_face = unknown_person[top:bottom, left:right]


# pyplot.title("unknown_face")
# pyplot.imshow(unknown_face)
# pyplot.show()

# enc_unknown_face = face_recognition.face_encodings(unknown_face)

# pyplot.imshow(enc_unknown_face)
# pyplot.show()

# for face in known_face_list:
#       enc_known_face = face_recognition.face_encodings(face)

#   distance = face_recognition.face_distance(enc_known_face, enc_unknown_face[0])

#   pyplot.title("distance: " + str(distance))
#   pyplot.imshow(face)
#   pyplot.show()
