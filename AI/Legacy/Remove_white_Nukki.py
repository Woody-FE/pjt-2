from PIL import Image

img = Image.open('./images/hat.jpg')
img = img.convert('RGBA')
datas = img.getdata()

newData = []
cutOff = 255

for item in datas:
    if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("Remove_white_image.png", "PNG")
