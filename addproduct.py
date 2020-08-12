import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image

con = sqlite3.connect('products.db')
cur = con.cursor()

defaultImg = 'img/store.png'


class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Product')
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(1450,150,350,550)
        self.setFixedSize(self.size())
        self.Ui()
        self.show()

    def Ui(self):
        self.widgets()
        self.layout()

    def widgets(self):
        ################ Top Widgets #########################
        self.addProductImg = QLabel()
        self.img = QPixmap('icons/addproduct.png')
        self.addProductImg.setPixmap(self.img)
        self.titletext = QLabel('Add Product')
        ####### Bottom ###################
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText('Enter the name of Product')
        self.manufacturerEntry = QLineEdit()
        self.manufacturerEntry.setPlaceholderText('Enter the name of Manufacturer')
        self.priceEntry = QLineEdit()
        self.priceEntry.setPlaceholderText("Enter the price")
        self.QuotaEntry = QLineEdit()
        self.QuotaEntry.setPlaceholderText('Enter the quota of the product')
        self.uploadBtn = QPushButton('Upload')
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.submitBtn = QPushButton('Submit')
        self.submitBtn.clicked.connect(self.addProduct)

    def layout(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        self.topLayout.addWidget(self.addProductImg)
        self.topLayout.addWidget(self.titletext)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel('Name'), self.nameEntry)
        self.bottomLayout.addRow(QLabel('Manufacturer'), self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel('Price'), self.priceEntry)
        self.bottomLayout.addRow(QLabel('Quota'), self.QuotaEntry)
        self.bottomLayout.addRow(QLabel('Upload'), self.uploadBtn)
        self.bottomLayout.addRow(QLabel(''), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)

    def uploadImg(self):
        global defaultImg
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image File (*.jpg *.png)")
        if ok:
            print(self.filename)
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img/{}".format(defaultImg))


    def addProduct(self):
        global defaultImg
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = self.priceEntry.text()
        quota = self.QuotaEntry.text()


        if (name and manufacturer and price and quota !=""):
            try:
                query="INSERT INTO 'products' (product_name,product_manufacturer,product_price,product_qouta,product_img) VALUES(?,?,?,?,?)"
                cur.execute(query,(name,manufacturer,price,quota,defaultImg))
                con.commit()
                QMessageBox.information(self,"Info","Product has been added")

            except Exception as e:
                print(e)
                QMessageBox.information(self, "Info", "Product has not been added")

        else:
            QMessageBox.information(self, "Info", "Fields cant be empty!!!")
