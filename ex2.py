from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.Qt import *


class Widget1(QtWidgets.QLabel):  # QWidget
    def __init__(self, parent=None):
        super(Widget1, self).__init__(parent)
        self.setText("Widget1")
        self.setStyleSheet("background-color: #f00;")

    def leaveEvent(self, event):
        print('class Widget1: leaveEvent')

    def enterEvent(self, event):
        print('class Widget1: enterEvent')

        def mouseMoveEvent(self, event):
            if \
                    self.coords[0] + 75 <= event.x() <= self.coords[0] - 75 and self.coords[1] + 23 <= event.y() <= \
                            self.coords[1] - 23:
                self.coords[0] = random.randint(0, self.w - self.btn_size[0])
                self.coords[1] = random.randint(0, self.h - self.btn_size[1])
            self.pushButton_no.move(*self.coords)


class Widget2(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Widget2, self).__init__(parent)
        self.setText("Widget2")
        self.setStyleSheet("background-color: #00f;")

    def leaveEvent(self, event):
        print('class Widget2: leaveEvent')

    def enterEvent(self, event):
        print('class Widget2: enterEvent')


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        wid1 = Widget1(self)
        wid2 = Widget2(self)

        layout = QVBoxLayout(self)
        layout.addWidget(wid1)  # , alignment=Qt.AlignCenter
        layout.addWidget(wid2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Widget()
    window.resize(300, 300)
    window.show()
    sys.exit(app.exec_())