import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line Edit')
        self.setGeometry(50,50,350,350)
        self.Ui()

    def Ui(self):
        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.setPlaceholderText("Please Enter the Name")
        self.nameTextbox.move(150,50)
        self.passTextbox = QLineEdit(self)
        self.passTextbox.setPlaceholderText('Enter the Password')
        self.passTextbox.setEchoMode(QLineEdit.Password) # To make the password no visible
        self.passTextbox.move(150,80)
        button = QPushButton('Save', self)
        button.setGeometry(170, 130,80,30)
        button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name = self.nameTextbox.text()
        password = self.passTextbox.text()
        print(name, password)


def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()