import sys
from random import randint
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap

font = QFont('Times', 12)
computerScore=0
playerScore=0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello Bro')
        self.setGeometry(350,150,500,500)
        self.Ui()

    def Ui(self):
        self.cscore = QLabel('Computer Score : ', self)
        self.cscore.move(30, 20)
        self.cscore.setFont(font)
        self.pscore = QLabel('Player Score : ', self)
        self.pscore.move(330, 20)
        self.pscore.setFont(font)

        self.ImageComputer = QLabel(self)
        self.ImageComputer.setPixmap(QPixmap('rock.png'))
        self.ImageComputer.move(30, 60)
        self.ImagePlayer = QLabel(self)
        self.ImagePlayer.setPixmap(QPixmap('rock.png'))
        self.ImagePlayer.move(330, 60)
        self.ImageGame = QLabel(self)
        self.ImageGame.setPixmap(QPixmap('game.png'))
        self.ImageGame.move(230, 100)

        self.startBtn = QPushButton('Start', self)
        self.startBtn.move(160, 200)
        self.startBtn.clicked.connect(self.start)
        self.stopBtn = QPushButton('Stop', self)
        self.stopBtn.move(250, 200)
        self.stopBtn.clicked.connect(self.stop)

        self.timer = QTimer(self)
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def start(self):
        print('start')
        self.timer.start()

    def playGame(self):
        print('playing')
        self.rndComputer = randint(1, 3)
        self.rndPlayer = randint(1, 3)
        print(self.rndPlayer, self.rndComputer)

        if self.rndComputer == 1:
            self.ImageComputer.setPixmap(QPixmap("rock.png"))
        elif self.rndComputer == 2:
            self.ImageComputer.setPixmap(QPixmap("paper.png"))
        else:
            self.ImageComputer.setPixmap(QPixmap("scissors.png"))

        if self.rndPlayer == 1:
            self.ImagePlayer.setPixmap(QPixmap("rock.png"))

        elif self.rndPlayer == 2:
            self.ImagePlayer.setPixmap(QPixmap("paper.png"))
        else:
            self.ImagePlayer.setPixmap(QPixmap("scissors.png"))

    def stop(self):
        print('stop')
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndPlayer == self.rndComputer:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.rndPlayer == 1 and self.rndComputer == 2:
            mbox = QMessageBox.information(self, "Information", "You Lose")
            playerScore +=1
            self.cscore.setText("Your Score:{}".format(computerScore))
        elif self.rndPlayer == 1 and self.rndComputer == 3:
            mbox = QMessageBox.information(self, "Information", "Win")
            computerScore +=1
            self.pscore.setText("Computer Score:{}".format(computerScore))
        elif self.rndPlayer == 2 and self.rndComputer == 3:
            mbox = QMessageBox.information(self, "Information", "You Lose")
            computerScore +=1
            self.cscore.setText("Computer Score:{}".format(computerScore))
        elif self.rndPlayer == 2 and self.rndComputer == 1:
            mbox = QMessageBox.information(self, "Information", "You win")
            computerScore +=1
            self.cscore.setText("Computer Score:{}".format(playerScore))
        else:
            pass






def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()