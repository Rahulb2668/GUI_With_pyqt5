import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(50,50,350,350)
        self.Ui()

    def Ui(self):
        text1 = QLabel('I am here for testing', self)
        text2 = QLabel('I am ready with you maaahn',self)
        text2.move(200,50)
        self.show()


def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()