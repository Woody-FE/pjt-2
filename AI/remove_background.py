from PIL import Image
import face_recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = face_recognition.load_image_file("./images/91.jpg")
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
    pil_image.save("./images/baby.jpg")

# 얼굴에서 배경제거 코드 구현
# 얼굴 동화풍으로 transfer 코드 구현

# im = cv2.imread("./images/baby.jpg")
# cv2.imshow('original',im)
# mask = np.zeros(im.shape[:2],np.uint8)
# rect = (box[0][0], box[0][1], box[0][2]-box[0][0], box[0][3]-box[0][1])
# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)
# cv2.grabCut(im,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# if len(np.where((mask==3)|(mask==1))[0])>0:
#     mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#     mask2 = np.repeat(mask2[:,:,np.newaxis],3,axis=2)
# else:
#     mask2 = np.zeros_like(im)
#     mask2[box[0][1]:box[0][3],box[0][0]:box[0][2],:] = 1
# im2 = im*mask2
# cv2.imshow('post-grabcut',im2)
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(mask)
# flag, mask = cv2.threshold(mask, maxVal-1, 255, cv2.cv.CV_THRESH_BINARY)
# cv2.imshow("mask", mask)
# b, g, r = cv2.split(im2)
# img_RGBA = cv2.merge((b, g, r, mask))
# cv2.imshow("final",img_RGBA)