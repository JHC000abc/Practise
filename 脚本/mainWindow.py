
from PyQt5.QtWidgets import *
import sys
from Practise.脚本 import untitled


class Example(QLabel):
    def __init__(self):
        super().__init__()
        self.ui = untitled.Ui_Form1()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.slot_pushbutton_clicked)
        self.click_signal = 0


    # def slot_pushbutton_clicked(self):
    #     if self.click_signal == 0:
    #         self.ui.pushButton.setText('缩小')
    #         self.ui.label.mode = 1
    #         self.click_signal = 1
    #
    #     else:
    #         self.ui.pushButton.setText('放大')
    #         self.ui.label.mode = 0
    #         self.click_signal = 0

    def enterEvent(self,a0):
        print("123")
        # return super().enterEvent(a0)

    def leaveEvent(self,a0):
        print("321")
        # return super().leaveEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = Example()
    x.show()
    sys.exit(app.exec_())