import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal


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
        self.close()

    def moveButton(self):
        self.coords[0] = random.randint(0, self.width() - self.btn_size[0])
        self.coords[1] = random.randint(0, self.height() - self.btn_size[1])
        self.btn.move(*self.coords)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())