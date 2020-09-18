import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("./AIrang/images/baby.jpg")
image_gray = cv2.imread("./AIrang/images/baby.jpg", cv2.IMREAD_GRAYSCALE)

b, g, r = cv2.split(image)
image2 = cv2.merge([r, g, b])

# plt.imshow(image2)
# plt.xticks([])
# plt.yticks([])
# plt.show()

# cv2.imshow('image', image)
# cv2.imshow('image_gray', image_gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

blur = cv2.GaussianBlur(image_gray, ksize=(3, 3), sigmaX=0)
ret, thresh1 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

edged = cv2.Canny(blur, 10, 250)
cv2.imshow('Edged', edged)
# cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closed', closed)
# cv2.waitKey(0)

contours, _ = cv2.findContours(
    closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0

contours_image = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('contours_image', contours_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours_xy = np.array(contours)
contours_xy.shape
