import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import random
from PyQt5.QtCore import pyqtSignal

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('maindesugn.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.setMouseTracking(True)
        self.lupabutton.clicked.connect(self.lupa)
        self.kartatabutton.clicked.connect(self.kartata)
        self.settingsbutton.clicked.connect(self.settings)
        self.shapkakabutton.clicked.connect(self.shapkala)
        self.coords = [240, 310]
        self.btn_size = [75, 23]
        self.w = 350
        self.h = 450

    def lupa(self):
        self.stackedWidget.setCurrentIndex(3)

    def shapkala(self):
        self.stackedWidget.setCurrentIndex(1)

    def kartata(self):
        self.stackedWidget.setCurrentIndex(2)

    def settings(self):
        self.setMouseTracking(True)
        self.stackedWidget.setCurrentIndex(4)

    def mouseMoveEvent(self, event):
        print('pisa')
        if \
                self.coords[0] + 75 <= event.x() <= self.coords[0] - 75 and self.coords[1] + 23 <= event.y() <= \
                        self.coords[1] - 23:
            self.coords[0] = random.randint(0, self.w - self.btn_size[0])
            self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        self.pushButton_no.move(*self.coords)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    sys.exit(app.exec())
