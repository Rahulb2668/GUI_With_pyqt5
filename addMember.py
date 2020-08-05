import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


con = sqlite3.connect('products.db')
cur = con.cursor()


class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Product')
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(1450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.Ui()
        self.show()

    def Ui(self):
        self.Widgets()
        self.Layouts()

    def Widgets(self):
        self.addMemberImg = QLabel()
        self.Img = QPixmap('icons/addmember.png')
        self.addMemberImg.setPixmap(self.Img)
        self.addMemberImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Add Member")
        self.titleText.setAlignment(Qt.AlignCenter)


        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText('Enter the Name')
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText('Enter the SurName')
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText('Enter the Phone Number')

        self.submitbtn = QPushButton('Submit')
        self.submitbtn.clicked.connect(self.addMember)

    def Layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addMemberImg)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel('Name: '), self.nameEntry)
        self.bottomLayout.addRow(QLabel('Surname'), self.surnameEntry)
        self.bottomLayout.addRow(QLabel('Phone: '), self.phoneEntry)
        self.bottomLayout.addRow(QLabel(''), self.submitbtn)

        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)

    def addMember(self):
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()

        if name and surname and phone != "":
            try:
                query = "insert into 'members' (member_name, member_surname, member_phone) values(?, ?, ?)"
                cur.execute(query, (name, surname, phone))
                con.commit()
                QMessageBox.information(self, 'info', "Member has added")
                self.nameEntry.setText("")
                self.surnameEntry.setText("")
                self.phoneEntry.setText("")

            except:
                QMessageBox.information(self, 'info', "Member has not added")

        else:
            QMessageBox.information(self, 'info', "Fields cannot be empty")



