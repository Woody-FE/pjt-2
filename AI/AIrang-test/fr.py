from PIL import Image
import face_recognition

img_path = "./AIrang/images/baby.jpg"

# Load the jpg file into a numpy array
img = face_recognition.load_image_file(img_path)

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(img)
chin = face_landmarks_list[0]['chin']
# print('chin', chin)

# 누끼 코드
# img = Image.open(img_path)
# img = img.convert("RGBA")
# datas = img.getdata()
# newData = []

# for item in datas:
#     # 여기에 face_recognition 좌표로 조건
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))

#     else:
#         newData.append(item)
#         img.putdata(newData)

print(1)

# png 확장자로 저장
# img.save("./NukkiedImage.png", "PNG")
