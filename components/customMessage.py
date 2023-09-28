from PySide6.QtWidgets import (
    QMessageBox,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QDialog,
)
from PySide6.QtGui import QIcon


class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)

    def set_custom_icon(self, icon):
        self.setIconPixmap(icon)
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)


class MsgInformation(QDialog):
    def __init__(self, title, system, message, time):
        super().__init__()
        self.setWindowTitle(title)

        self.layout = QVBoxLayout()

        self.name_s = QLabel(f"Sistema de Drones: {system}")
        self.message_s = QLabel(f"Mensaje enviado: {message}")
        self.time_s = QLabel(f"Tiempo óptimo: {time}")

        self.layout.addWidget(self.name_s)
        self.layout.addWidget(self.message_s)
        self.layout.addWidget(self.time_s)

        self.button = QPushButton("OK")
        self.button.clicked.connect(self.close)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.setFixedSize(300, 200)


def correct_msgbox(title, text):
    msg_box = MsgBox(title, text)
    msg_box.exec()


def error_msgbox(title, text):
    msg_box = MsgBox(title, text)
    msg_box.exec()


def alert_msgbox(title, text):
    msg_box = MsgBox(title, text)
    msg_box.exec()


def information_msgbox(title, system, message, time):
    msg_box = MsgInformation(title, system, message, time)
    msg_box.exec()
