import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 400, 400)
        self.Ui()


    def Ui(self):
        mainlayout = QVBoxLayout()
        toplayout = QHBoxLayout()
        buttonlayout = QHBoxLayout()

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        bt1 = QPushButton()
        bt2 = QPushButton()
        toplayout.addWidget(cbox)
        toplayout.addWidget(rbtn)
        toplayout.addWidget(combo)
        # toplayout.setContentsMargins(100, 10, 20, 20)
        buttonlayout.addWidget(bt1)
        buttonlayout.addWidget(bt2)
        buttonlayout.setContentsMargins(100, 10, 20, 20)
        mainlayout.addLayout(toplayout)
        mainlayout.addLayout(buttonlayout)

        self.setLayout(mainlayout)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()