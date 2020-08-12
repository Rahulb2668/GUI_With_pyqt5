import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 600, 600)
        self.Ui()

    def Ui(self):
        self.gridlayout = QGridLayout()
        btn1 = QPushButton('Button1')
        btn2 = QPushButton('Button2')
        btn3 = QPushButton('Button3')
        btn4 = QPushButton('Button4')

        self.gridlayout.addWidget(btn1, 0,0)
        self.gridlayout.addWidget(btn2, 0,1)
        self.gridlayout.addWidget(btn3, 0,2)
        self.gridlayout.addWidget(btn4, 0,3)

        # btn1 = QPushButton('Button1')
        self.setLayout(self.gridlayout)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()