import cv2
import numpy as np
import face_recognition as fr

img_path = "./AIrang/images/hyj.png"
# original image
# -1 loads as-is so if it will be 3 or 4 channel as the original
origin_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
BGRA_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2BGRA)
image = BGRA_img

fr_img = fr.load_image_file(img_path)
fr_landmarks_list = fr.face_landmarks(fr_img)
fr_chin = fr_landmarks_list[0]['chin']

# mask defaulting to black for 3-channel and transparent for 4-channel
# (of course replace corners with yours)
mask = np.zeros(image.shape, dtype=np.uint8)
roi_corners = np.array(
    [fr_chin], dtype=np.int32)
# print(fr_chin)
# roi_corners = np.array(
#     [[(0, 0), (0, 300), (200, 0)]], dtype=np.int32)
# fill the ROI so it doesn't get wiped out when the mask is applied
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255, )*channel_count
cv2.fillPoly(mask, roi_corners, ignore_mask_color)
# from Masterfool: use cv2.fillConvexPoly if you know it's convex

# apply the mask
masked_image = cv2.bitwise_and(image, mask)

# save the result
cv2.imwrite('image_masked.png', masked_image)
