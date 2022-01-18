import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from Practise.test import Ui_Form
from Practise.expend_label import ExpandLabel

class EventFilterWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # widget = QWidget()
        # label = QLabel()
        # label.setText("这是标签")
        #
        # # button = QPushButton("Trigger event!")
        # # button.installEventFilter(self)
        #
        # hbox = QHBoxLayout()
        # hbox.addWidget(label)
        # # hbox.addWidget(button)
        # widget.setLayout(hbox)
        # self.setCentralWidget(widget)
        # self.show()

    def enterEvent(self, a0):
        print("123")
        # return super().enterEvent(a0)

    def leaveEvent(self, a0):
        print("321")
        # return super().leaveEvent(a0)


def main():
    app = QApplication(sys.argv)
    window = EventFilterWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()