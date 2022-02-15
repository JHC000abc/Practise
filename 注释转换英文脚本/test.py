#!/usr/bin/env python
# encoding: utf-8
import cv2
from PyQt5.QtGui import QImage, QPixmap


def set_img(self, img_src):
    '''
        设置label中的图片显示
    '''
    self.img = cv2.imread(img_src, 0)
    showImage = QImage(self.img.data, self.img.shape[1], self.img.shape[0], QImage.Format_Indexed8)
    self.setPixmap(QPixmap.fromImage(showImage))


def changeBloack(self, img_src):
    '''
        设置反色
    '''
    gray = cv2.imread(img_src, 0)
    if self.flag2 == 1:
        dst = 255 - gray
        showImage = QImage(dst.data, dst.shape[1], dst.shape[0], QImage.Format_Indexed8)
        self.setPixmap(QPixmap.fromImage(showImage))
        self.flag2 = 0
    else:
        showImage = QImage(gray.data, gray.shape[1], gray.shape[0], QImage.Format_Indexed8)
        self.setPixmap(QPixmap.fromImage(showImage))
        self.flag2 = 1