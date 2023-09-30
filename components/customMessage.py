from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QDialog,
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from icons.iconos import Icons
from PySide6.QtSvgWidgets import QSvgWidget
from components.styles import Styles


class MsgBox(QDialog):
    def __init__(self, title, text, icon, color):
        super().__init__()
        self.setWindowTitle(title)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.panel = QWidget(self)
        self.layout = QVBoxLayout()

        self.panel_svg = QWidget()
        self.layout_svg = QVBoxLayout(self.panel_svg)

        self.svg = QSvgWidget(icon)
        # self.panel.setStyleSheet("background-color:#13151b")
        self.svg.setMaximumSize(QSize(65, 65))
        self.svg.setStyleSheet("border:0px")
        self.layout_svg.addWidget(self.svg)

        self.layout.addWidget(self.panel_svg, alignment=Qt.AlignCenter)
        self.panel_svg.setStyleSheet("border:0px")
        self.title = QLabel(f"{title}")
        self.title.setStyleSheet("color:white;font-weight:600;border:0px")
        self.layout.addWidget(self.title, alignment=Qt.AlignCenter)
        self.text = QLabel(f"{text}")
        self.text.setStyleSheet("color:white;border:0px")
        self.layout.addWidget(self.text, alignment=Qt.AlignCenter)
        self.button = QPushButton("Ok")
        self.button.clicked.connect(self.close)
        self.button.setStyleSheet(Styles.BTN_ALERT)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.setFixedSize(380, 240)
        self.setStyleSheet(f"background-color:#1a1a1f;border-top:3px solid #{color}")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_startPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_startPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = False


class MsgInformation(QDialog):
    def __init__(self, title, system, message, time):
        super().__init__()
        # self.setWindowTitle(title)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.layout = QVBoxLayout()

        self.panel_svg = QWidget()
        self.layout_svg = QVBoxLayout(self.panel_svg)

        self.svg = QSvgWidget(Icons.ICON_INFO)
        # self.panel.setStyleSheet("background-color:#13151b")
        self.svg.setMaximumSize(QSize(65, 65))
        self.svg.setStyleSheet("border:0px")
        self.layout_svg.addWidget(self.svg)

        self.layout.addWidget(self.panel_svg, alignment=Qt.AlignCenter)
        self.panel_svg.setStyleSheet("border:0px")

        self.name_s = QLabel(f"Sistema de Drones: {system}")
        self.name_s.setStyleSheet(Styles.WHITE_INFO)
        self.message_s = QLabel(f"Mensaje enviado: {message}")
        self.message_s.setStyleSheet(Styles.WHITE_INFO)
        self.time_s = QLabel(f"Tiempo óptimo: {time}")
        self.time_s.setStyleSheet(Styles.WHITE_INFO)

        self.layout.addWidget(self.name_s)
        self.layout.addWidget(self.message_s)
        self.layout.addWidget(self.time_s)

        self.button = QPushButton("OK")
        self.button.setStyleSheet(Styles.BTN_ALERT)
        self.button.clicked.connect(self.close)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.setFixedSize(390, 280)
        self.setStyleSheet("background-color:#1a1a1f;border-top:3px solid #33a9ff")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_startPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_startPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = False


def correct_msgbox(title, text):
    msg_box = MsgBox(title, text, Icons.ICON_CHECK, "5be3a4")
    msg_box.exec()


def error_msgbox(title, text):
    msg_box = MsgBox(title, text, Icons.ICON_ERROR, "f96179")
    msg_box.exec()


def alert_msgbox(title, text):
    msg_box = MsgBox(title, text, Icons.ICON_ALERT, "eecf7e")
    msg_box.exec()


def information_msgbox(title, system, message, time):
    msg_box = MsgInformation(title, system, message, time)
    msg_box.exec()
