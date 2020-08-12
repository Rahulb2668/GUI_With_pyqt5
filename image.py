import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Testing Image working')
        self.setGeometry(50,50,500,500)
        self.Ui()

    def Ui(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('download.jpg'))
        self.label.move(150,50)
        button = QPushButton('Close',self)
        button.clicked.connect(self.closeim)
        button1 = QPushButton('open',self)
        button1.clicked.connect(self.openim)
        button1.move(0,50)
        self.show()

    def closeim(self):
        self.label.close()

    def openim(self):
        self.label.show()


def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()