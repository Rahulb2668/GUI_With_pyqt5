import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(250,150,500,500)
        self.Ui()

    def Ui(self):
        self.name = QLineEdit(self)
        self.name.move(150,50)
        self.name.setPlaceholderText('Enter the name')
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText('Enter the surname')
        self.surname.move(150, 80)
        button = QPushButton('Submit', self)
        button.move(150, 140)
        button.clicked.connect(self.getvalue)
        self.male = QRadioButton('Male', self)
        self.male.move(150, 110)
        self.male.setChecked(True)
        self.female= QRadioButton('Female', self)
        self.female.move(200, 110)
        self.show()

    def getvalue(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            gender = 'male'
        else:
            gender = 'female'
        print(name, surname, gender )



def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()