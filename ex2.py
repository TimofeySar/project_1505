class black_mainwindow(QMainWindow):
    def __init__(self):
        print(1)
        super().__init__()
        uic.loadUi('maindesugn_black.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.lupabutton_1.clicked.connect(self.poisk)
        self.kartatabutton_1.clicked.connect(self.mappa)
        self.settingsbutton_1.clicked.connect(self.nastroike)
        self.shapkakabutton_1.clicked.connect(self.shapka)
        self.coords_1 = [240, 310]
        self.btn_size_1 = [75, 23]
        self.w_black = 350
        self.h = 450

    def poisk(self):
        self.button_home_2.clicked.connect(self.home)
        self.stackedWidget.setCurrentIndex(3)
        self.Naity.clicked.connect(self.vibor)

    def shapka(self):
        self.stackedWidget.setCurrentIndex(1)
        self.button_home12.clicked.connect(self.home)

    def mappa(self):
        self.stackedWidget.setCurrentIndex(2)
        self.button_home_1.clicked.connect(self.home)
        black_mainwindow.hide(self)
        main()
        black_mainwindow.show(self)
        self.stackedWidget.setCurrentIndex(0)

    def nastroike(self):
        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_ocenla.clicked.connect(self.dialogus)
        self.button_home_3.clicked.connect(self.home)
        self.pushButton_tema.clicked.connect(self.temacka)

    def dialogus(self):
        self.dialog_copy_2 = Example()
        self.dialog_copy_2.show()

    def delitel(self):
        self.lineEdit.clear()

    def show_dialog_2(self):
        item = self.listWidget.currentItem()
        item = str(item.text())
        Info_window_copy = InfoWindow_2(item)
        Info_window_copy.exec()

    def home(self):
        self.stackedWidget.setCurrentIndex(0)

    def temacka(self):
        pass

    def vibor(self):
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
            self.listWidget.clicked.connect(lambda: self.show_dialog_2())


class InfoWindow_2(QDialog):
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