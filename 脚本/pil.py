from PIL import Image

im = Image.open('ImageFileForAI_Female_front.bmp')
# 灰度
img1 = im.convert("L")

img1.show()

