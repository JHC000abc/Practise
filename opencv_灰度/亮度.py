# 调整灰度图像的亮度和对比度
import cv2 as cv
import numpy as np

img = cv.imread('./1022745_m_MC20210901-002_0.bmp')
# 增加图像亮度
# 注意需要使用cv.add(),不能直接x+y
res1 = np.uint8(np.clip((cv.add(1.5*img,0)), 0, 255))
# 增加图像对比度
res2 = np.uint8(np.clip((cv.add(1*img,0)), 0, 255))
tmp = np.hstack((img, res1, res2))  # 三张图片横向合并（便于对比显示）

cv.imshow('image', tmp)
cv.waitKey(0)
cv.destroyAllWindows()