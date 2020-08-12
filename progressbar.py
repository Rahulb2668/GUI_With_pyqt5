import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 500, 500)
        self.Ui()

    def Ui(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.pbar = QProgressBar()
        btn1 = QPushButton('Start')
        btn1.clicked.connect(self.starttimer)
        btn2 = QPushButton('Stop')
        btn2.clicked.connect(self.stoptimer)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.runpbar)
        vbox.addWidget(self.pbar)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()

    def starttimer(self):
        self.timer.start()

    def stoptimer(self):
        self.timer.stop()

    def runpbar(self):
        global count
        count+=1
        self.pbar.setValue(count)
        if count == 100:
            self.stoptimer()
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()