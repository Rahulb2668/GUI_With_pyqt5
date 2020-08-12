import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import addproduct
import addMember
import os
from PIL import Image

con = sqlite3.connect('products.db')
cur = con.cursor()

productId = 0

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Product Manager')
        self.setWindowIcon(QIcon('Icons/icon.ico'))
        self.setGeometry(1400, 100, 1350, 750)
        self.setFixedSize(self.size())

        self.Ui()
        self.show()

    def Ui(self):
        self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layouts()
        self.displayProducts()
        self.displayMember()

    def toolBar(self):
        self.tb = self.addToolBar('Tool Bar')
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addProduct = QAction(QIcon('icons/add.png'), 'Add Product', self)
        self.tb.addAction(self.addProduct)
        self.addProduct.triggered.connect(self.funcAddProduct)
        self.tb.addSeparator()

        self.addMember = QAction(QIcon('icons/users.png'), 'Add Member', self)
        self.tb.addAction(self.addMember)
        self.addMember.triggered.connect(self.funcAddMember)
        self.tb.addSeparator()

        self.sellProduct = QAction(QIcon('icons/sell.png'), 'Sell Product', self)
        self.tb.addAction(self.sellProduct)
        self.tb.addSeparator()

    def tabWidget(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, 'Products')
        self.tabs.addTab(self.tab2, 'Members')
        self.tabs.addTab(self.tab3, 'Statitcs')

    def widgets(self):
        ######### Tab1 #############
        # Main Left Layout Widget
        self.productTable = QTableWidget()
        self.productTable.setColumnCount(6)
        self.productTable.setColumnHidden(0, True)
        self.productTable.setHorizontalHeaderItem(0, QTableWidgetItem('Product Id'))
        self.productTable.setHorizontalHeaderItem(1, QTableWidgetItem('Product Name'))
        self.productTable.setHorizontalHeaderItem(2, QTableWidgetItem('Manufacturer'))
        self.productTable.setHorizontalHeaderItem(3, QTableWidgetItem('Price'))
        self.productTable.setHorizontalHeaderItem(4, QTableWidgetItem('Quota'))
        self.productTable.setHorizontalHeaderItem(5, QTableWidgetItem('Availability'))
        self.productTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.productTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.productTable.doubleClicked.connect(self.selectedProduct)

        # Right Top layouy widget
        self.searchText = QLabel('Search')
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText('Search For Products')
        self.searchBtn = QPushButton('Search')

        # Right Middle layout widget

        self.allProducts = QRadioButton('All Products')
        self.availableProducts = QRadioButton('Available')
        self.notavailableProducts = QRadioButton('Not Available')
        self.listButton = QPushButton('List')

        ################## Tab2########################

        self.memberTable = QTableWidget()
        self.memberTable.setColumnCount(4)
        self.memberTable.setHorizontalHeaderItem(0, QTableWidgetItem('Member Id'))
        self.memberTable.setHorizontalHeaderItem(1, QTableWidgetItem('Member Name'))
        self.memberTable.setHorizontalHeaderItem(2, QTableWidgetItem('Member SurName'))
        self.memberTable.setHorizontalHeaderItem(3, QTableWidgetItem('Phone'))
        self.memberSearchText = QLabel('Search Member')
        self.memberSearchEntry = QLineEdit()
        self.memberSearchEntry.setPlaceholderText('Search the Member')
        self.memberSearchButton = QPushButton('Search')

    def layouts(self):
        '''Tab1'''
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QVBoxLayout()
        self.mainRightLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QHBoxLayout()
        self.topGroupBox = QGroupBox('Search Box')  # If you want to use style sheets in layouts you have to use Groupbox
        self.MiddleGroupBox = QGroupBox('List Box')

        # Table layout
        self.mainLeftLayout.addWidget(self.productTable)

        # Right Top
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchBtn)
        self.topGroupBox.setLayout(self.rightTopLayout)
        self.mainRightLayout.addWidget(self.topGroupBox)

        # Right Middle
        self.rightMiddleLayout.addWidget(self.allProducts)
        self.rightMiddleLayout.addWidget(self.availableProducts)
        self.rightMiddleLayout.addWidget(self.notavailableProducts)
        self.rightMiddleLayout.addWidget(self.listButton)
        self.MiddleGroupBox.setLayout(self.rightMiddleLayout)
        self.mainRightLayout.addWidget(self.MiddleGroupBox)
        # Adding to Main Layout
        self.mainLayout.addLayout(self.mainLeftLayout, 70)
        self.mainLayout.addLayout(self.mainRightLayout, 30)

        self.tab1.setLayout(self.mainLayout)

        ''' Tab2 '''

        self.memberMainLayout = QHBoxLayout()
        self.memberLeftLayout = QHBoxLayout()
        self.memberRightLayout = QHBoxLayout()
        self.memberRightGroupBox = QGroupBox('Search For Members')
        self.memberRightGroupBox.setContentsMargins(10, 10, 10, 600)

        self.memberRightLayout.addWidget(self.memberSearchText)
        self.memberRightLayout.addWidget(self.memberSearchEntry)
        self.memberRightLayout.addWidget(self.memberSearchButton)
        self.memberRightGroupBox.setLayout(self.memberRightLayout)

        self.memberLeftLayout.addWidget(self.memberTable)

        self.memberMainLayout.addLayout(self.memberLeftLayout, 70)
        self.memberMainLayout.addWidget(self.memberRightGroupBox)

        self.tab2.setLayout(self.memberMainLayout)
        
    def funcAddProduct(self):
        self.newProduct = addproduct.AddProduct()

    def funcAddMember(self):
        self.newMember = addMember.AddMember()

    def displayProducts(self):
        for i in reversed(range(self.productTable.rowCount())):
            self.productTable.removeRow(i)
        query = cur.execute("select product_id, product_name, product_manufacturer, product_price, product_qouta, product_availability from products")
        for row_data in query:
            row_number = self.productTable.rowCount()
            self.productTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.productTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def displayMember(self):
        for i in reversed(range(self.memberTable.rowCount())):
            self.memberTable.removeRow(i)
        members = cur.execute ("select * from members")
        for row_data in members:
            row_number = self.memberTable.rowCount()
            self.memberTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.memberTable.setItem(row_number,column_number, QTableWidgetItem(str(data)))
        self.memberTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def selectedProduct(self):
        global productId
        listProduct = []
        for i in range(0,6):
            listProduct.append(self.productTable.item(self.productTable.currentRow(),i).text())
        productId = listProduct[0]
        try:
            self.product = DisplayProduct()
        except Exception as e:
            print(e)


class DisplayProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Product Details')
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(1450,150,350,600)
        self.setFixedSize(self.size())
        self.Ui()
        self.show()

    def Ui(self):
        self.productDetails()
        self.Widgets()
        self.Layouts()


    def productDetails(self):
        global productId
        query = cur.execute('select * from products where product_id =?', (productId,)).fetchone()
        self.productName = query[1]
        self.productManufacturer = query[2]
        self.productPrice = query[3]
        self.productQouta = query[4]
        self.productImg = query[5]
        self.productStatus = query[6]


    def Widgets(self):
        self.titleText = QLabel('Update Product')
        self.product_Img = QLabel()
        self.Img = QPixmap('img/{}'.format(self.productImg))
        self.product_Img.setPixmap(self.Img)
        self.product_Img.setAlignment(Qt.AlignCenter)
        self.titleText.setAlignment(Qt.AlignCenter)

        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.productName)
        self.manufacturerEntry = QLineEdit()
        self.manufacturerEntry.setText(self.productManufacturer)
        self.priceEntry = QLineEdit()
        self.priceEntry.setText(str(self.productPrice))
        self.QuotaEntry = QLineEdit()
        self.QuotaEntry.setText(str(self.productQouta))
        self.availabilityCombo = QComboBox()
        self.availabilityCombo.addItems(['Avaialble', 'Unavailable'])

        self.uploadBtn = QPushButton('Upload')
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.updateBtn = QPushButton('Update')
        self.updateBtn.clicked.connect(self.updateProduct)
        self.deleteBtn = QPushButton('Delete')
        self.deleteBtn.clicked.connect(self.deleteProduct)

    def uploadImg(self):
        size = (256,256)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'UploadImage', '', 'Image Files (*.jpg *.png)')
        if ok :
            self.productImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save('img/{}'.format(self.productImg))

    def updateProduct(self):
        global productId
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = int(self.priceEntry.text())
        qouta = int(self.QuotaEntry.text())
        status = self.availabilityCombo.currentText()
        defaultImg = self.productImg

        if name and manufacturer and price and qouta != "":
            try:
                query = 'update products set product_name = ?, product_manufacturer =?, product_price=?, product_qouta = ?, product_img=?, product_availability=? where product_id=?'
                cur.execute(query,(name, manufacturer, price, qouta, defaultImg, status, productId))
                con.commit()
                QMessageBox.information(self, 'intro', 'Product is updated')
            except:
                QMessageBox.information(self, 'intro', 'Product is not updated')
        else:
            QMessageBox.information(self, 'intro', 'Fields cannot be empty')


    def deleteProduct(self):
        global productId
        mbox = QMessageBox.question(self, 'Warning', 'Are you sure to delete', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                cur.execute('delete from products where product_id=?', (productId, ))
                con.commit()
                QMessageBox.information(self, 'intro', 'Product is Deleted')
            except:
                QMessageBox.information(self, 'intro', 'Product is not Deleted')


    def Layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.product_Img)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel('Name : '), self.nameEntry)
        self.bottomLayout.addRow(QLabel('Manufacturer'), self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel('Price'), self.priceEntry)
        self.bottomLayout.addRow(QLabel('Qouta'), self.QuotaEntry)
        self.bottomLayout.addRow(QLabel('Status'), self.availabilityCombo)
        self.bottomLayout.addRow(QLabel('Image'), self.uploadBtn)
        self.bottomLayout.addRow(QLabel(''), self.deleteBtn)
        self.bottomLayout.addRow(QLabel(''), self.updateBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)



def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
