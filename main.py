import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QDialog
import random
from PyQt5.QtCore import pyqtSignal
from urllib import request
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont, QCursor
import pygame, requests, os, math
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from flask import Flask, render_template
from flask.helpers import url_for
import datetime


class chachech(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('cochesh.ui', self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.kekek.clicked.connect(self.kekekekek)

    def kekekekek(self):
        self.dialog_copyy = dialog()
        self.dialog_copyy.show()
        self.close()


class dialog(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('otzif.ui', self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
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
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
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
        try:
            self.listWidget.clicked.connect(self.show_dialog)
        except:
            pass

    def lupa(self):
        self.button_home_2.clicked.connect(self.homi)
        self.stackedWidget.setCurrentIndex(3)
        self.Naity.clicked.connect(self.select)
        self.krestik.clicked.connect(self.ydai)
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
        self.matshrut_1.clicked.connect(self.openURL_1)
        self.matshrut_2.clicked.connect(self.openURL_2)
        self.matshrut_3.clicked.connect(self.openURL_3)
        self.matshrut_4.clicked.connect(self.openURL_4)
        self.matshrut_5.clicked.connect(self.openURL_5)
        self.matshrut_6.clicked.connect(self.openURL_6)

    def openURL_1(self):
        url = QUrl("http://127.0.0.1:8080/first")  # Замените на нужный URL
        QDesktopServices.openUrl(url)

    def openURL_2(self):
        url = QUrl("http://127.0.0.1:8080/second")  # Замените на нужный URL
        QDesktopServices.openUrl(url)

    def openURL_3(self):
        url = QUrl("http://127.0.0.1:8080/third")  # Замените на нужный URL
        QDesktopServices.openUrl(url)

    def openURL_4(self):
        url = QUrl("http://127.0.0.1:8080/forth")  # Замените на нужный URL
        QDesktopServices.openUrl(url)

    def openURL_5(self):
        url = QUrl("http://127.0.0.1:8080/fifth")  # Замените на нужный URL
        QDesktopServices.openUrl(url)

    def openURL_6(self):
        url = QUrl("http://127.0.0.1:8080/third")  # Замените на нужный URL
        QDesktopServices.openUrl(url)

    def kartata(self):
        self.stackedWidget.setCurrentIndex(2)
        self.button_home_1.clicked.connect(self.homi)
        mainwindow.hide(self)
        main()
        mainwindow.show(self)
        self.stackedWidget.setCurrentIndex(0)

    def settings(self):
        self.black_window = black_mainwindow()
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
            mainwindow.hide(self)
            window.close()
        else:
            window.show()
            mainwindow.close(self)

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
            print(1234)




class Info_window(QDialog):
    def __init__(self, item):
        super().__init__()
        uic.loadUi('vidget.ui', self)
        self.item = str(item)
        self.connn = sqlite3.connect("moscow_landmarks.db")
        cur = self.connn.cursor()
        req = cur.execute("""SELECT * FROM landmarks WHERE 
                               name = ?""",
                          (self.item,)).fetchall()
        try:
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
            try:
                data = request.urlopen(str(req[0][4])).read()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                scaled_pixmap = pixmap.scaled(self.label_5.size(), Qt.KeepAspectRatio)

                # Устанавливаем масштабированное изображение в QLabel
                self.label_5.setPixmap(scaled_pixmap)


            except:

                self.label_5.setText("no picture")
        except:
            pass


class MapParams(object):
    def __init__(self):
        self.lat = 55.75482  # Координаты центра карты на старте. Задал координаты университета
        self.lon = 37.62169
        self.zoom = 16  # Масштаб карты на старте. Изменяется от 1 до 19
        self.type = "map"  # Другие значения "sat", "sat,skl"
        self.my_step = 0.003

    def update(self, event):
        print(event.key)
        if event.key == 1073741899 and self.zoom < 19:  # Page_UP
            self.zoom += 1
        elif event.key == 1073741902 and self.zoom > 2:  # Page_DOWN
            self.zoom -= 1
        elif event.key == 1073741904:  # LEFT_ARROW
            self.lon -= self.my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 1073741903:  # RIGHT_ARROW
            self.lon += self.my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 1073741906 and self.lat < 85:  # UP_ARROW
            self.lat += self.my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 1073741905 and self.lat > -85:  # DOWN_ARROW
            self.lat -= self.my_step * math.pow(2, 15 - self.zoom)

    # Преобразование координат в параметр ll, требуется без пробелов, через запятую и без скобок
    def ll(self):
        return str(self.lon) + "," + str(self.lat)


# Создание карты с соответствующими параметрами.
def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapParams()
    # создание объекта Clock
    clock = pygame.time.Clock()

    # установка FPS
    FPS = 60
    map_file = None
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.KEYDOWN:  # Обрабатываем различные нажатые клавиши.
                mp.update(event)
            map_file = load_map(mp)
            # Рисуем картинку, загружаемую из только что созданного файла.
            screen.blit(pygame.image.load(map_file), (0, 0))
            pygame.display.flip()

        clock.tick(FPS)  # Ограничение FPS

    pygame.quit()
    # Удаляем файл с изображением.
    if map_file is not None:
        os.remove(map_file)


def open_mainwindow():
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    sys.exit(app.exec())


# черная тема

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
        try:
            self.listWidget.itemActivated.connect(lambda item: self.show_dialog(item))
            self.listWidget.installEventFilter(self)
        except:
            pass
        self.h = 450

    def eventFilter(self, obj, event):
        if obj == self.listWidget and event.type() == QEvent.MouseButtonRelease:
            item = self.listWidget.itemAt(event.pos())
            if item:
                self.show_dialog(item)
        return super(black_mainwindow, self).eventFilter(obj, event)

    def closeApp(self):
        black_mainwindow.close(self)

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
            self.select()
        else:
            self.old_keyPressEvent(event)


    def shapkala(self):
        self.stackedWidget.setCurrentIndex(1)
        self.button_home12.clicked.connect(self.homi)
        self.matshrut_1.clicked.connect(self.openURL_1)
        self.matshrut_2.clicked.connect(self.openURL_2)
        self.matshrut_3.clicked.connect(self.openURL_3)
        self.matshrut_4.clicked.connect(self.openURL_4)
        self.matshrut_5.clicked.connect(self.openURL_5)
        self.matshrut_6.clicked.connect(self.openURL_6)


def openURL_1(self):
    url = QUrl("http://127.0.0.1:8080/first")  # Замените на нужный URL
    QDesktopServices.openUrl(url)


def openURL_2(self):
    url = QUrl("http://127.0.0.1:8080/second")  # Замените на нужный URL
    QDesktopServices.openUrl(url)


def openURL_3(self):
    url = QUrl("http://127.0.0.1:8080/third")  # Замените на нужный URL
    QDesktopServices.openUrl(url)


def openURL_4(self):
    url = QUrl("http://127.0.0.1:8080/forth")  # Замените на нужный URL
    QDesktopServices.openUrl(url)


def openURL_5(self):
    url = QUrl("http://127.0.0.1:8080/fifth")  # Замените на нужный URL
    QDesktopServices.openUrl(url)


def openURL_6(self):
    url = QUrl("http://127.0.0.1:8080/third")  # Замените на нужный URL
    QDesktopServices.openUrl(url)

    def kartata(self):
        self.stackedWidget.setCurrentIndex(2)
        self.button_home_1.clicked.connect(self.homi)
        mainwindow.hide(self)
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

    def show_dialog(self, item):
        print(2)
        item_text = item.text()
        Info_window_copy = Info_window(item_text)

        # Устанавливаем флаги окна
        Info_window_copy.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)

        # Отображаем окно
        Info_window_copy.exec()
    def homi(self):
        self.stackedWidget.setCurrentIndex(0)

    def toggle_window(self, window):
        if window.isVisible():
            mainwindow.hide(self)
            window.close()
        else:
            window.show()
            mainwindow.close(self)

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



if __name__ == '__main__':
    open_mainwindow()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365)

@app.route("/fifth")
def home():
    return render_template("home.html")

@app.route("/forth")
def home_1():
    return render_template("home_1.html")

@app.route("/first")
def home_2():
    return render_template("trip1.html")

@app.route("/second")
def home_3():
    return render_template("jor2.html")

@app.route("/third")
def home_4():
    return render_template("trip3.html")


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')