# import cv2
# import os
import face_recognition
import numpy
from PIL import Image
# from PIL import Image, ImageDraw
# from IPython.display import Image, display
# from matplotlib import pyplot

image = face_recognition.load_image_file(
    "AIrang/images/family2.jpg")
face_locations = face_recognition.face_locations(image)
PIL_image = Image.open("AIrang/images/family2.jpg")

# 얼굴인식 확인
face_index = 0
for face in face_locations:
    top, right, bottom, left = face[0], face[1], face[2], face[3]
    cropFace = PIL_image.crop((left, top, right, bottom))
    cropFaceName = "face" + str(face_index) + ".jpg"
    face_index += 1
    cropFace.save(cropFaceName)

# pyplot.rcParams["figure.figsize"] = (16, 16)
# pyplot.imshow(image)
