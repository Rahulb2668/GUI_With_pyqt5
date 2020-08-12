import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line Edit')
        self.setGeometry(50, 50, 350, 350)
        self.Ui()

    def Ui(self):
        self.nameTextbox = QLineEdit(self)
        self.nameTextbox.setPlaceholderText("Please Enter the Name")
        self.nameTextbox.move(100, 50)
        self.list_widget = QListWidget(self)
        self.list_widget.move(100, 80)
        savbtn = QPushButton('Delete all', self)
        savbtn.setGeometry(400, 80, 80, 30)
        savbtn.clicked.connect(self.deleteall)
        cancelbtn = QPushButton('Delete', self)
        cancelbtn.setGeometry(400, 110, 80, 30)
        cancelbtn.clicked.connect(self.cancel)
        addbtn = QPushButton('Add', self)
        addbtn.setGeometry(400, 140, 80, 30)
        addbtn.clicked.connect(self.add)
        button = QPushButton('exit', self)
        button.setGeometry(400, 170, 80, 30)
        button.clicked.connect(self.exit_)
        list1  = ['Batman', 'Superman', 'Spiderman', 'Ironman']
        self.list_widget.addItems(list1)
        self.show()

    def add(self):
        value = self.nameTextbox.text()
        self.list_widget.addItem(value)
        self.nameTextbox.setText("")

    def cancel(self):
        print(self.list_widget.currentItem().text())
        id = self.list_widget.currentRow()
        self.list_widget.takeItem(id)

    def deleteall(self):
        self.list_widget.clear()
    def exit_(self):
        sys.exit()

def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()