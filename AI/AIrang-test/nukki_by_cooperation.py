from PIL import Image
# 누끼컷으로 변경할 이미지
img = Image.open('./face1.jpg')
img = img.convert("RGBA")
datas = img.getdata()
newData = []


for item in datas:
    print(item)
    # 여기에 face_recognition 좌표로 조건
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))

    else:
        newData.append(item)
        img.putdata(newData)

# png 확장자로 저장
# img.save("./NukkiedImage.png", "PNG")
