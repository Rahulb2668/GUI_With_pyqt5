import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(50,50,500,500)
        self.Ui()

    def Ui(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Enter your name')
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText('Enter the surname')
        self.name.move(150,50)
        self.surname.move(150,80)
        self.rem = QCheckBox('Remeber Me', self)
        self.rem.move(150,110)
        button = QPushButton('Save', self)
        button.move(250,110)
        button.clicked.connect(self.save)
        self.show()

    def save(self):
        if self.rem.isChecked():
            print(self.name.text(), self.surname.text())
        else:
            print('Not checked')


def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()