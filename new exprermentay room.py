import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QDialog
import random
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtGui import QFont, QCursor
import pygame, requests, os, math
from PyQt5.QtCore import Qt, QEvent, QPoint


class black_mainwindow(QMainWindow):
    def __init__(self, parent=None):
        print(1)
        super(black_mainwindow, self).__init__(parent)
        uic.loadUi('maindesugn_black.ui', self)
        self.centralwidget.setStyleSheet("#centralwidget {border-radius: 5px;}")
        self.setMouseTracking(True)
        self.m_drag = False
        self.m_DragPosition = QPoint()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.stackedWidget.setCurrentIndex(0)
        self.lupabutton.clicked.connect(self.lupa)
        self.kartatabutton.clicked.connect(self.kartata)
        self.settingsbutton.clicked.connect(self.settings)
        self.shapkakabutton.clicked.connect(self.shapkala)
        self.green_button.clicked.connect(self.minimizeApp)
        self.red_button.clicked.connect(self.closeApp)
        self.yellow_button.clicked.connect(self.doNothing)
        self.drag = False
        self.DragPosition = QPoint()
        self.coords = [240, 310]
        self.btn_size = [75, 23]
        self.w = 350
        self.h = 450

    def closeApp(self):
        #mainwindow.close(self)

    def doNothing(self):
        pass

    def minimizeApp(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.y() < 30:  # Здесь 30 - это высота верхней части окна
                self.drag = True
                self.DragPosition = QCursor.pos() - self.pos()
                event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.drag:
                self.move(QCursor.pos() - self.DragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        self.drag = False

    def lupa(self):
        self.button_home_2.clicked.connect(self.homi)
        self.stackedWidget.setCurrentIndex(3)
        self.Naity.clicked.connect(self.select)
        self.old_keyPressEvent = self.keyPressEvent
        self.keyPressEvent = self.new_keyPressEvent

    def new_keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            # Показываем кнопку при нажатии Enter
            self.select()
        else:
            # Для всех других клавиш вызываем оригинальный метод
            self.old_keyPressEvent(event)

    def shapkala(self):
        self.stackedWidget.setCurrentIndex(1)
        self.button_home12.clicked.connect(self.homi)

    def kartata(self):
        self.stackedWidget.setCurrentIndex(2)
        self.button_home_1.clicked.connect(self.homi)
        #mainwindow.hide(self)
        main()
        mainwindow.show(self)
        self.stackedWidget.setCurrentIndex(0)

    def settings(self):
        self.black_window = mainwindow()
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_ocenla.clicked.connect(self.dialog)
        self.button_home_3.clicked.connect(self.homi)
        self.pushButton_tema.clicked.connect(lambda checked: self.toggle_window(self.black_window))

    def dialog(self):
        self.dialog_copy = Example()
        self.dialog_copy.show()

    def ydai(self):
        self.lineEdit.clear()

    def show_dialog(self):
        item = self.listWidget.currentItem()
        item = str(item.text())
        Info_window_copy = Info_window(item)
        Info_window_copy.exec()

    def homi(self):
        self.stackedWidget.setCurrentIndex(0)

    def toggle_window(self, window):
        if window.isVisible():
            #mainwindow.hide(self)
            window.close()
        else:
            window.show()
            #mainwindow.close(self)

    def select(self):
        self.con = sqlite3.connect("moscow_landmarks.db")
        self.listWidget.clear()
        req = (f"SELECT DISTINCT name FROM landmarks WHERE "
               f"name"
               f" LIKE ?")
        cur = self.con.cursor()
        param = self.lineEdit.text()
        paramtor = param
        param = param.capitalize()
        paramtrue = '%' + param + '%'
        print(paramtrue)

        result = cur.execute(
            req,
            (paramtrue,)).fetchall()
        print(result)
        if result == []:
            paramtor = paramtor.upper()
            print(paramtor)
            paramtrue1 = '%' + paramtor + '%'
            result = cur.execute(
                req,
                (paramtrue1,)).fetchall()
            print(result)
        for elem in result:
            self.listWidget.addItem(elem[0])

        if not result:
            self.listWidget.addItem('Неверный запрос')
            self.listWidget.addItem('Похоже такой достопремечательности нет в москве:(')
        else:
            self.listWidget.clicked.connect(lambda: self.show_dialog())


class Info_window_black(QDialog):
    def __init__(self, item):
        super().__init__()
        uic.loadUi('vidget.ui', self)
        self.item = str(item)
        self.connn = sqlite3.connect("moscow_landmarks.db")
        cur = self.connn.cursor()
        req = cur.execute("""SELECT * FROM landmarks WHERE 
                               name = ?""",
                          (self.item,)).fetchall()
        info_text = str(req[0][2])
        result = ' '.join(info_text.split())
        print(len(result))
        print(result)
        if 1300 > len(result) > 600:
            font = QFont("Arial", 11)
        elif len(result) < 600:
            font = QFont("Arial", 13)
        else:
            font = QFont("Arial", 8)
        self.label.setText(item)
        self.label_3.setText(str(req[0][3]))
        self.label_4.setText(result)
        self.label_4.setWordWrap(True)
        self.label.setWordWrap(True)
        self.label_4.setFont(font)


def open_mainwindow():
    app = QApplication(sys.argv)
    ex = black_mainwindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    open_mainwindow()
