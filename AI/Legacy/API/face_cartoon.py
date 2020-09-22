from PIL import Image
import face_recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 얼굴 인식
image = face_recognition.load_image_file("./images/white.jpg")
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    pil_image.save('./images/face.jpg')

# # 누끼컷으로 변경할 이미지(흰색 배경)
img = Image.open('./images/trans.jpg')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if 245 <= item[0] <= 255 and 245 <= item[1] <= 255 and 245 <= item[2] <= 255:
        newData.append((255,255,255,0))

    else:
        newData.append(item)
img.putdata(newData)

# png 확장자로 저장
img.save("Transparent.png", "PNG")

# cartoonizer 이미지

cv_img = cv2.imread('.images/baby.jpg', cv2.IMREAD_COLOR)

cartoon_img = cv2.stylization(cv_img, sigma_s=100, sigma_r=0.5)

cv2.imshow('original', cv_img)
cv2.imshow('cartoon1', cartoon_img)
