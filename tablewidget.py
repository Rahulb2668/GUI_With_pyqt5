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

        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Class'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Mark'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('Average'))
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()

        # Adding items to the table
        self.table.setItem(0, 0, QTableWidgetItem('Rahul'))
        self.table.setItem(0, 1, QTableWidgetItem('EEE'))
        self.table.setItem(0, 2, QTableWidgetItem('50'))
        self.table.setItem(0, 3, QTableWidgetItem('50'))

        self.table.setItem(1, 0, QTableWidgetItem('Appuz'))
        self.table.setItem(1, 1, QTableWidgetItem('EEE'))
        self.table.setItem(1, 2, QTableWidgetItem('100'))
        self.table.setItem(1, 3, QTableWidgetItem('50'))
        self.table.doubleClicked.connect(self.get)
        # To make the table umeditable use the trigger function
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        btn = QPushButton('Get')
        btn.clicked.connect(self.get)
        vbox.addWidget(self.table)
        vbox.addWidget(btn)

        self.setLayout(vbox)
        self.show()

    def get(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()