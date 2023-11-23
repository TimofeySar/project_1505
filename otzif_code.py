import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QWidget

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
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dialog()
    ex.show()
    sys.exit(app.exec())