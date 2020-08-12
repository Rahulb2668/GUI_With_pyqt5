 import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello maahn')
        self.setGeometry(250, 150, 500, 500)
        self.Ui()

    def Ui(self):
        self.cl = QLabel(self)
        self.cl.resize(150,100)
        self.cl.setStyleSheet("background-color:green")
        self.cl.move(50,50)

        btn1 = QPushButton('start', self)
        btn1.move(250,50)
        btn2 = QPushButton('stop', self)
        btn2.move(250,100)
        btn1.clicked.connect(self.startTimer)
        btn2.clicked.connect(self.stopTimer)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changecolor)
        self.value = 0
        self.show()


    def changecolor(self):
        if self.value ==0:
            self.cl.setStyleSheet("background-color:yellow")
            self.value = 1
        else:
            self.cl.setStyleSheet('background-color:red')
            self.value = 0

    def startTimer(self):
        self.timer.start()

    def stopTimer(self):
        self.timer.stop()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()