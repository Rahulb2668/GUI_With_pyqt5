import sys
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal layout')
        self.setGeometry(350, 150, 400, 400)
        self.Ui()


    def Ui(self):
        menu = self.menuBar()
        file = menu.addMenu('File')
        edit = menu.addMenu('Edit')
        code = menu.addMenu('Code')
        helpMenu = menu.addMenu('Help')

        # SUb menus
        new = QAction("New", self)
        new.setShortcut('Ctrl+N')
        file.addAction(new)
        open = QAction('Open', self)
        file.addAction(open)

        exit = QAction('Exit', self)
        # For menu we use triggered instead for clicked
        exit.triggered.connect(self.exitFunc)
        # To set icon
        # import QIcon from QtGui
        # exit.setIcon(QIcon('Image'))

        file.addAction(exit)
        self.show()

    def exitFunc(self):
        mbox = QMessageBox.information(self, 'Warning', 'Are you sure to exit', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()