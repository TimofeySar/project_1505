from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        # Создаем виджет для размещения кнопок
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Добавляем кнопку в макет
        self.button = QPushButton("Button", self)
        self.button.hide()  # Скрываем кнопку по умолчанию
        layout.addWidget(self.button)

        # Переопределяем метод keyPressEvent для главного окна
        self.old_keyPressEvent = self.keyPressEvent
        self.keyPressEvent = self.new_keyPressEvent

    def new_keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            # Показываем кнопку при нажатии Enter
            self.button.show()
        else:
            # Для всех других клавиш вызываем оригинальный метод
            self.old_keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
