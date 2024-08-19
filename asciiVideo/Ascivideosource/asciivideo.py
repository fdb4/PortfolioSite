from PIL import Image
from numpy import asarray
img=Image.open('test.jpg')
data=asarray(img)

imgy=[]
grayscale="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for x in data:
    imgx = []
    for y in x:
        imgx.append((y[0]+y[1]+y[2])/3)
    imgy.append(imgx.copy())

print(grayscale[0])


