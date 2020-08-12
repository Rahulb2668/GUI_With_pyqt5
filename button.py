import sys
from PyQt5.QtWidgets import *
from functools import partial


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Learning about Button')
        self.setGeometry(50,50,350,350)
        self.Ui()

    def Ui(self):
        self.text = QLabel('Hello Buddy', self)
        button = QPushButton('Press here', self)
        button.move(100,100)
        button.clicked.connect(partial(self.pressed, 'hello'))
        self.show()

    def pressed(self,text):
        self.text.setText(text)

def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()