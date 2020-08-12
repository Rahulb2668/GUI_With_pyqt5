import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times",16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(250,150,500,500)
        self.Ui()

    def Ui(self):
        self.spinbox = QSpinBox(self)
        self.spinbox.setFont(font)
        self.spinbox.move(150,100)
        # self.spinbox.setMinimum(25)
        # self.spinbox.setMaximum(100)
        self.spinbox.setRange(25, 121)
        self.spinbox.setSuffix('cm')
        # self.spinbox.valueChanged.connect(self.getvalue)
        button = QPushButton('send',self)
        button.move(150,140)
        button.clicked.connect(self.getvalue)
        self.show()

    def getvalue(self):
        print(self.spinbox.value())

def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()