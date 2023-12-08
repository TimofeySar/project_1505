import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QDialog
import random
from PyQt5.QtCore import pyqtSignal
class chachech(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('cochesh.ui', self)
        self.kekek.clicked.connect(self.kekekekek)

    def kekekekek(self):
        self.dialog_copyy = dialog()
        self.dialog_copyy.show()
        self.close()
class dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('otzif.ui', self)
        self.Thanks.clicked.connect(self.rite)
        self.bygirl.clicked.connect(self.privet)


    def rite(self):
        if not self.otzif.text():
            self.close()
        with open("reviews.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        with open("reviews.txt", 'a+', encoding='utf-8') as file:
            print(lines)
            bitit = len(lines) + 1
            print(bitit, self.otzif.text(), file=file)
            print(self.otzif.text())

        self.close()
    def privet(self):
        self.dialog_copyyy = chachech()
        self.dialog_copyyy.show()
        self.close()

class Button(QPushButton):
    mouseMoved = pyqtSignal()

    def mouseMoveEvent(self, event):
        self.mouseMoved.emit()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.coords = [300, 250]
        self.btn_size = [120, 40]
        self.d = 15
        self.w = 500
        self.h = 400
        self.setGeometry(300, 300, self.w, self.h)
        self.setWindowTitle('Убегающая кнопка')
        self.label = QLabel(self)
        self.label.setText("Вам нравится наш проект?")
        self.label.move(170, 30)
        self.label.resize(160, 40)

        self.button = QPushButton(self)
        self.button.setText("Да")
        self.button.move(100, 250)
        self.button.resize(*self.btn_size)
        self.button.clicked.connect(self.okletsgo)


        self.btn = Button(self)
        self.btn.setMouseTracking(True)
        self.btn.setText("нет")
        self.btn.resize(*self.btn_size)
        self.btn.move(*self.coords)
        self.btn.mouseMoved.connect(self.moveButton)
        self.show()

    def okletsgo(self):
        self.dialog_copyy = dialog()
        self.dialog_copyy.show()
        self.close()

    def moveButton(self):
        self.coords[0] = random.randint(0, self.width() - self.btn_size[0])
        self.coords[1] = random.randint(0, self.height() - self.btn_size[1])
        self.btn.move(*self.coords)


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('maindesugn.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.lupabutton.clicked.connect(self.lupa)
        self.kartatabutton.clicked.connect(self.kartata)
        self.settingsbutton.clicked.connect(self.settings)
        self.shapkakabutton.clicked.connect(self.shapkala)
        self.coords = [240, 310]
        self.btn_size = [75, 23]
        self.w = 350
        self.h = 450



    def lupa(self):
        self.button_home_2.clicked.connect(self.homi)
        self.stackedWidget.setCurrentIndex(3)

    def shapkala(self):
        self.stackedWidget.setCurrentIndex(1)
        self.button_home12.clicked.connect(self.homi)

    def kartata(self):
        self.stackedWidget.setCurrentIndex(2)
        self.button_home_1.clicked.connect(self.homi)

    def settings(self):
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_ocenla.clicked.connect(self.dialog)
        self.button_home_3.clicked.connect(self.homi)
        self.temaa.clicked.connect(self.tema)

    def dialog(self):
        self.dialog_copy = Example()
        self.dialog_copy.show()

    def homi(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    sys.exit(app.exec())
