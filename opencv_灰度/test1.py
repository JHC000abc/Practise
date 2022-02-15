
import cv2
import numpy as np
alpha = 0.3
beta = 80
img_path = r"C:\Users\JHC\Desktop\paint_cv\Practise\opencv_灰度\1022745_m_MC20210901-002_0.bmp"
img = cv2.imread(img_path)
img2 = cv2.imread(img_path)
def updateAlpha(x):
    global alpha, img, img2
    alpha = cv2.getTrackbarPos('Alpha', 'image')
    alpha = alpha * 0.01
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))
def updateBeta(x):
    global beta, img, img2
    beta = cv2.getTrackbarPos('Beta', 'image')
    img = np.uint8(np.clip((alpha * img2 + beta), 0, 255))