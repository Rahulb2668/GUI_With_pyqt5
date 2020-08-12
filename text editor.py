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
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)
        button = QPushButton('Click here', self)
        button.setFont(font)
        button.move(330, 280)
        button.clicked.connect(self.mbox)
        self.show()

    def mbox(self):
        val = self.editor.toPlainText()
        print(val)

def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()