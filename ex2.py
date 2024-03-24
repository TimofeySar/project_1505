import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Open URL Example')

        # Создание кнопки
        self.button = QPushButton('Open URL', self)
        self.button.clicked.connect(self.openURL)
        self.button.setGeometry(50, 50, 200, 50)

        self.show()

    def openURL(self):
        url = QUrl("http://127.0.0.1:8080/third")  # Замените на нужный URL
        QDesktopServices.openUrl(url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())