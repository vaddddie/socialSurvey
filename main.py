import random
import sys

from PyQt5 import QtWidgets as qT
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont


class Window(QMainWindow):
    def __init__(self, question):
        super(Window, self).__init__()

        if question is None:
            question = "Я прав?"

        self.setWindowTitle("Социальный опрос")
        self.setGeometry(600, 300, 600, 400)

        self.titleText = qT.QLabel(self)
        self.titleText.setText(question)
        self.titleText.setFont(QFont("Arial", 45))
        self.titleText.move(210, 10)
        self.titleText.adjustSize()

        self.btnY = qT.QPushButton(self)
        self.btnY.move(185, 100)
        self.btnY.setFont(QFont("Arial", 15))
        self.btnY.setText("Да")
        self.btnY.adjustSize()

        self.btnN = qT.QPushButton(self)
        self.btnN.move(330, 100)
        self.btnN.setFont(QFont("Arial", 15))
        self.btnN.setText("Нет")
        self.btnN.adjustSize()



class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()

        self.setGeometry(700, 300, 300, 200)

        self.main_Text = qT.QLabel(self)
        self.main_Text.setText("Я так и знал!")
        self.main_Text.setFont(QFont('Arial', 20))
        self.main_Text.move(80, 20)
        self.main_Text.adjustSize()


class Main:
    def __init__(self, question):
        self.app = QApplication(sys.argv)
        self.firstWindow = Window(question)
        self.secondWindow = SecondWindow()


    def CallFirstWindow(self):
        self.firstWindow.btnY.clicked.connect(self.CallSecondWindow)
        self.firstWindow.btnN.enterEvent = self.Moving
        self.firstWindow.show()

    def CallSecondWindow(self):
        self.secondWindow.show()

    def Moving(self, event):
        self.firstWindow.btnN.move(random.randint(10, 490), random.randint(50, 150))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    for index in range(1, len(sys.argv)):
        if sys.argv[index] == "-q" and index + 1 < len(sys.argv):
            main = Main(sys.argv[index + 1])
            break
    else:
        main = Main(None)

    main.CallFirstWindow()

    sys.exit(app.exec_())

