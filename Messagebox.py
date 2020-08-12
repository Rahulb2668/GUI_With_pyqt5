import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times",12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(250,150,500,500)
        self.Ui()

    def Ui(self):
        button = QPushButton('Click here', self)
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.mbox)
        self.show()

    def mbox(self):
        # mbox = QMessageBox.question(self, 'Warning!', 'Are you sure to exit', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        # if mbox == QMessageBox.Yes:
        #     sys.exit()
        # elif mbox == QMessageBox.No:
        #     print('you Clicked no')
        # else:
        #     print('Pressed cancel')
        mbox = QMessageBox.information(self,'Helo Bro', 'Chumma')


def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()