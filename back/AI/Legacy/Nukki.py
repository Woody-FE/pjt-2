import cv2
import numpy as np
import face_recognition as fr


# original image path
img_path = "./images/team/kti2_Shinkai.jpg"
img_name = img_path[9:]

# -1 loads as-is so if it will be 3 or 4 channel as the original
origin_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
BGRA_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2BGRA)
image = BGRA_img
chin_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

# face recognition landmark 'chin'
fr_img = fr.load_image_file(img_path)
fr_landmarks_list = fr.face_landmarks(fr_img)
fr_chin = fr_landmarks_list[0]['chin']

# make numpy array
np_fr_chin = np.array(fr_chin)
fr_chin_bottom = np.max(np_fr_chin, axis=0)[1]

chin_y = np_fr_chin[:, 1:]

min_chin_idx = np.argmax(chin_y)
chin_x = np_fr_chin[min_chin_idx]

chin_start, chin_end = np_fr_chin[0], np_fr_chin[-1]

# middle chin
chin_middle = (0.5 * (chin_start[0] + chin_end[0]),
               0.5 * (chin_start[1] + chin_end[1]))

# upper head boundary
upper_head = []
for i in range(len(np_fr_chin)-1, -1, -1):
    if i < len(np_fr_chin) % 2:
        temp = (np_fr_chin[i][0], 0.85*(chin_start[1] -
                                        (np_fr_chin[i][1]-chin_start[1])))
    else:
        temp = (np_fr_chin[i][0], 0.85*(chin_end[1] -
                                        (np_fr_chin[i][1]-chin_end[1])))

    upper_head.append(temp)

# over eyelash cut
fr_left_eyebrow = fr_landmarks_list[0]['left_eyebrow']
fr_right_eyebrow = fr_landmarks_list[0]['right_eyebrow']

bump = 0.05 * (chin_end[0] - chin_start[0])

min_y = 0.8 * min(np.min(fr_left_eyebrow, axis=0)[
    1], np.min(fr_right_eyebrow, axis=0)[1])
eyelash_left_start = (chin_start[0] + bump, min_y)
eyelash_right_end = (chin_end[0] - bump, min_y)

# mask defaulting to black for 3-channel and transparent for 4-channel
# (of course replace corners with yours)
nukki_coordinate = []
nukki_coordinate.append(eyelash_left_start)
nukki_coordinate.extend(fr_chin)
nukki_coordinate.append(eyelash_right_end)

mask = np.zeros(image.shape, dtype=np.uint8)
roi_corners = np.array(
    [nukki_coordinate], dtype=np.int32)

# fill the ROI so it doesn't get wiped out when the mask is applied
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255, )*channel_count
cv2.fillPoly(mask, roi_corners, ignore_mask_color)
# from Masterfool: use cv2.fillConvexPoly if you know it's convex

# apply the mask
Nukkied_image = cv2.bitwise_and(image, mask)

Trimmed_image = Nukkied_image.copy()
Trim_x = (int(chin_start[0]), int(chin_end[0]))
Trim_y = (int(min_y), int(fr_chin_bottom))
Trimmed_image = Nukkied_image[Trim_y[0]:Trim_y[1], Trim_x[0]:Trim_x[1]]

# image resize
Resized_image = cv2.resize(Trimmed_image, (180, 200), fx=1,
                           fy=1, interpolation=cv2.INTER_AREA)

# save the result
cv2.imwrite('Nukkied_image.png', Nukkied_image)
cv2.imwrite('Trimmed_image.png', Trimmed_image)
cv2.imwrite('Resized_image.png', Resized_image)
