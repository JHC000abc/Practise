from PyQt5.QtGui import QImage, QPixmap
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import test,expend_label


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = test.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.slot_pushbutton_clicked)
        self.click_signal = 0


    def slot_pushbutton_clicked(self):
        if self.click_signal == 0:
            self.ui.pushButton.setText('缩小')
            self.ui.label.mode = 1
            self.click_signal = 1

        else:
            self.ui.pushButton.setText('放大')
            self.ui.label.mode = 0
            self.click_signal = 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = Example()
    x.show()
    sys.exit(app.exec_())