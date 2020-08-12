import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 400, 400)
        self.Ui()


    def Ui(self):
        vbox = QVBoxLayout()
        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')

        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch()
        self.setLayout(vbox)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()