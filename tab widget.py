import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 600, 600)
        self.Ui()


    def Ui(self):
        mainlayout = QVBoxLayout()
        self.tab = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        vbox = QVBoxLayout()
        self.text1 = QLabel('Hello bro')
        vbox.addWidget(self.text1)
        vbox1 = QVBoxLayout()
        self.text1 = QLabel('Hello bro')
        vbox1.addWidget(self.text1)
        vbox2 = QVBoxLayout()
        self.text1 = QLabel('Hello bro')
        vbox2.addWidget(self.text1)
        vbox3 = QVBoxLayout()
        self.text1 = QLabel('Hello bro')
        vbox3.addWidget(self.text1)

        self.tab1.setLayout(vbox)
        self.tab2.setLayout(vbox1)
        self.tab3.setLayout(vbox2)
        self.tab4.setLayout(vbox3)

        self.tab.addTab(self.tab1, 'First')
        self.tab.addTab(self.tab2, 'Second')
        self.tab.addTab(self.tab3, 'Third')
        self.tab.addTab(self.tab4, 'last')

        mainlayout.addWidget(self.tab)

        self.setLayout(mainlayout)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()