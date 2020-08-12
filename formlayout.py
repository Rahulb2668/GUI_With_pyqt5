import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 400, 400)
        self.Ui()


    def Ui(self):
        form = QFormLayout()
        hbox = QHBoxLayout()
        # form.setRowWrapPolicy(QFormLayout.WrapAllRows)

        name_txt = QLabel("Name: ")
        name_input = QLineEdit()
        name_input.setPlaceholderText("Enter the name")

        pass_txt = QLabel("Password: ")
        pass_input = QLineEdit()
        pass_input.setPlaceholderText("Enter the password")

        form.addRow(name_txt, name_input)
        form.addRow(pass_txt, pass_input)
        form.addRow(QLabel("Country: "), QComboBox())

        # TO add more than oe wodget in a row create a hlayout and pass it to the addrow 

        hbox.addStretch()
        hbox.addWidget(QPushButton('Enter'))
        hbox.addWidget(QPushButton('Exit'))

        form.addRow(hbox)

        self.setLayout(form)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()