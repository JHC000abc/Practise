import random
from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic.properties import QtCore


AREA_SIZE = 240
MAX_EXPAND = 4
class ExpandLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.data = []
        self.data_color = []
        self.move_data = None
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.flag = False
        self.mode = 0
        self.single = 1
        self.setMouseTracking(True)
        self.pixmap = QPixmap()
        self.mypixmap = QPixmap()
        self.background = QPixmap()
        self.background.load("img.png")
        self.setPixmap(self.background)
        self.now_x = 0
        self.now_y = 0
        self.expend_num = MAX_EXPAND


    def wheelEvent(self, event):
        if self.mode == 1:
            angle = event.angleDelta()/10
            angleY = angle.y()
            if angleY > 0:
                self.slot_expend_num_add()
            else:
                self.slot_expend_num_reduce()


    def slot_expend_num_add(self):
        if self.expend_num == MAX_EXPAND:
            pass
        else:
            self.expend_num +=1
        self.init_paint_expand()

    def slot_expend_num_reduce(self):
        if self.expend_num == 1:
            pass
        else:
            self.expend_num -=1
        self.init_paint_expand()

    def init_paint_expand(self):
        expand_var = AREA_SIZE / self.expend_num
        rect = QRect(int(self.now_x) - expand_var / 2, int(self.now_y) - expand_var / 2, expand_var, expand_var)
        self.mode = 0
        self.update()
        self.mypixmap = self.grab(rect)
        width = self.mypixmap.width()
        height = self.mypixmap.height()
        self.pixmap = self.mypixmap.scaled(width * self.expend_num, height * self.expend_num,Qt.KeepAspectRatio)
        self.mode = 1
        self.update()

    def mousePressEvent(self, event):
        self.init_color()
        if event.button() == Qt.LeftButton:

            self.flag = True
            self.x0 = event.x()
            self.y0 = event.y()
            if self.flag == True and self.single == 1:
                self.x1 = self.x0 + self.change
                self.y1 = self.y0 + self.change
                self.setxy(self.x0, self.y0, self.x1, self.y1)
        elif event.button() == Qt.RightButton:
            x0 = event.x()
            y0 = event.y()
            for index, var in enumerate(self.data):
                if (x0 >= var[0] and x0 <= var[2]) and (y0 >= var[1] and y0 <= var[3]):
                    self.data.remove(var)
            if self.mode == 1:
                self.init_paint_expand()
        self.update()
        if self.mode == 1 and event.button == Qt.LeftButton:
            expand_var = AREA_SIZE / self.expend_num
            rect = QRect(int(self.now_x) - expand_var/2, int(self.now_y) - expand_var/2, expand_var, expand_var)
            self.mode = 0
            self.update()
            self.mypixmap = self.grab(rect)
            width = self.mypixmap.width()
            height = self.mypixmap.height()
            self.pixmap = self.mypixmap.scaled(width * self.expend_num, height * self.expend_num, Qt.KeepAspectRatio)
            self.mode = 1
            self.update()


    def init_color(self):
        if self.mode == 0:
            for i in range(len(self.data_color)):
                self.data_color[i] = Qt.red

    def mouseReleaseEvent(self, event):
        self.init_color()
        if event.button() == Qt.LeftButton:
            self.x1 = event.x()
            self.y1 = event.y()
            if self.x1 < self.x0 or self.y1 < self.y0:
                pass
            elif self.x1 == self.x0 or self.y1 == self.y0:
                self.setxy(self.x0, self.y0, self.x0 + 15, self.y0 + 15)
                self.flag = False
                self.update()
            else:
                self.setxy(self.x0, self.y0, self.x1, self.y1)
                self.move_data = None
                self.flag = False
                self.update()

    def mouseMoveEvent(self, event):
        self.now_x = event.x()
        self.now_y = event.y()
        self.single = 0
        if self.flag == True:
            if self.now_x < self.x0 or self.now_y < self.y0:
                pass
            else:
                self.x1 = event.x()
                self.y1 = event.y()
                self.move_data = [self.x0,self.y0,self.x1,self.y1]
                self.update()
        else:
            x2 = event.x()
            y2 = event.y()
            self.init_color()
            for index, var in enumerate(self.data):
                if (x2>=var[0] and x2 <=var[2]) and (y2>=var[1] and y2 <=var[3]):
                    self.data_color[index] = Qt.green
                else:
                    self.data_color[index] = Qt.red
            self.update()

        if self.mode == 1:
            expand_var = AREA_SIZE / self.expend_num
            self.init_paint_expand()
        self.update()


    def setxy(self, x1, y1, x2, y2):
        data = [x1, y1, x2, y2]
        self.data.append(data)
        self.data_color.append(Qt.red)




    def paintEvent(self, event):
        super().paintEvent(event)
        self.painter = QPainter()
        self.painter.begin(self)
        for index, data in enumerate(self.data):
            rect = QRect(data[0], data[1], abs(data[2] - data[0]), abs(data[3] - data[1]))
            self.painter.setPen(QPen(self.data_color[index], 2, Qt.SolidLine))
            self.painter.drawRect(rect)
        if self.move_data is not None:
            rect = QRect(self.move_data[0], self.move_data[1], abs(self.move_data[2] - self.move_data[0]), abs(self.move_data[3] - self.move_data[1]))
            self.painter.setPen(QPen(Qt.yellow, 2, Qt.SolidLine))
            self.painter.drawRect(rect)
        if self.mode == 1:
            self.painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            self.painter.drawPixmap(self.now_x,self.now_y,self.pixmap)
            self.painter.drawLine(self.now_x + AREA_SIZE/2-10, self.now_y+AREA_SIZE/2 , self.now_x +  AREA_SIZE/2+10,  self.now_y+AREA_SIZE/2)
            self.painter.drawLine(self.now_x +  AREA_SIZE/2, self.now_y+ AREA_SIZE/2-10 , self.now_x +  AREA_SIZE/2, self.now_y+ AREA_SIZE/2+10)
        self.painter.end()
