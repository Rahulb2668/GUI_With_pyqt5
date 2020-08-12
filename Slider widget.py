import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 400, 400)
        self.Ui()


    def Ui(self):
        vbox = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getValue)

        self.text1 = QLabel('0')
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2 = QLabel('Hello')

        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)
        self.setLayout(vbox)
        self.show()

    def getValue(self):
        val = self.slider.value()
        self.text2.setFont(QFont('Times', val))
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()