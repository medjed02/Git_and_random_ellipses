from random import randrange
import sys
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QWidget, QInputDialog, QErrorMessage, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor, QImage, QPalette, QBrush, QPainter, QFont


class Ellipses(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ellipses = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Случайные окружности')
        self.setGeometry(100, 100, 1200, 900)
        self.pushButton = QPushButton('Создать окружность', self)
        self.pushButton.setFont(QFont("Times", 20))
        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton.move(500, 400)
        self.pushButton.clicked.connect(self.new_ellipse)

    def new_ellipse(self):
        x, y, r = randrange(0, 1000), randrange(0, 800), randrange(1, 200)
        red, green, blue = randrange(0, 256), randrange(0, 256), randrange(0, 256)
        self.ellipses.append((x, y, r, red, green, blue))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        for el in self.ellipses:
            qp.setBrush(QColor(el[3], el[4], el[5]))
            qp.drawEllipse(el[0], el[1], el[2], el[2])