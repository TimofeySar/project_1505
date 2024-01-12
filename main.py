import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QDialog
import random
from PyQt5.QtCore import pyqtSignal
import main_blak as bl
from PyQt5.QtGui import QFont
import pygame, requests, os, math


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
        print(1)
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
        self.Naity.clicked.connect(self.select)
        self.krestik.clicked.connect(self.ydai)

    def shapkala(self):
        self.stackedWidget.setCurrentIndex(1)
        self.button_home12.clicked.connect(self.homi)

    def kartata(self):
        self.stackedWidget.setCurrentIndex(2)
        self.button_home_1.clicked.connect(self.homi)
        mainwindow.hide(self)
        main()
        mainwindow.show(self)
        self.stackedWidget.setCurrentIndex(0)

    def settings(self):
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_ocenla.clicked.connect(self.dialog)
        self.button_home_3.clicked.connect(self.homi)
        self.pushButton_tema.clicked.connect(self.tema)

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

    def tema(self):
        pass

    def select(self):
        self.con = sqlite3.connect("moscow_landmarks.db")
        self.listWidget.clear()
        req = (f"SELECT DISTINCT name FROM landmarks WHERE "
               f"name"
               f" LIKE ?")
        cur = self.con.cursor()
        param = self.lineEdit.text()
        paramtrue = '%' + param + '%'
        print(paramtrue)

        result = cur.execute(
            req,
            (paramtrue,)).fetchall()
        print(result)
        for elem in result:
            self.listWidget.addItem(elem[0])

        if not result:
            self.listWidget.addItem('Неверный запрос')
            self.listWidget.addItem('Похоже такой достопремечательности нет в москве:(')
        else:
            self.listWidget.clicked.connect(lambda: self.show_dialog())


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


class MapParams(object):
    def __init__(self):
        self.lat = 61.665279  # Координаты центра карты на старте. Задал координаты университета
        self.lon = 50.813492
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
    while True:
        flLeft = flRight = False
        event = pygame.event.wait()
        if event.type == pygame.QUIT:  # Выход из программы
            break
        elif event.type == pygame.KEYDOWN:  # Обрабатываем различные нажатые клавиши.
            mp.update(event)

            # Создаем файл
        map_file = load_map(mp)
        # Рисуем картинку, загружаемую из только что созданного файла.
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    # Удаляем файл с изображением.
    os.remove(map_file)


def open_mainwindow():
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    ex.hide()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    open_mainwindow()
