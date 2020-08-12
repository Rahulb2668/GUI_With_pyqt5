import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(250,150,500,500)
        self.Ui()

    def Ui(self):
        self.combo = QComboBox(self)
        self.combo.move(150,100)
        button = QPushButton('Save',self)
        button.move(150, 130)
        button.clicked.connect(self.getvalue)
        self.combo.addItem('Python')
        self.combo.addItems(['C++', 'C#', 'PHP'])
        self.show()

    def getvalue(self):
        val = self.combo.currentText()
        print(val)



def main():
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()