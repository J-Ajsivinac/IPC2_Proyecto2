from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QWidget,
    QSplitter,
    QStackedWidget,
    QFileDialog,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PySide6.QtGui import QFont
from PySide6 import QtCore
import sys
from modules.readFiles import Read
from Tdas.linkedListD import LinkedListDrone
from components.customMessage import *


class WindowP(QWidget):
    def __init__(self):
        super().__init__()
        self.drone_list = LinkedListDrone()
        self.s_list = LinkedListDrone()
        self.m_list = LinkedListDrone()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Proyecto 2")
        self.setStyleSheet("background-color: #202029;")
        self.layout_p = QVBoxLayout(self)
        self.layout_p.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self)
        self.stack = QStackedWidget(self)

        # Sidebar
        self.sidebar = QWidget(self)
        self.layout_sidebar = QVBoxLayout(self.sidebar)
        self.layout_sidebar.setContentsMargins(10, 220, 10, 10)
        self.sidebar.setStyleSheet("background-color: #1c1c24;")
        self.sidebar.setFixedWidth(220)
        self.layout_sidebar.setSpacing(20)

        self.btn_generate = self.custom_button(
            "Inicio", lambda: self.stack.setCurrentIndex(0)
        )
        self.btn_view_d = self.custom_button("Drones", self.change_view_dron)
        # self.btn_view_list = self.custom_button("Sistemas de Drones")
        self.btn_messages = self.custom_button(
            "Mensajes", lambda: self.stack.setCurrentIndex(2)
        )
        self.btn_help = self.custom_button(
            "Ayuda", lambda: self.stack.setCurrentIndex(3)
        )
        self.layout_sidebar.addWidget(self.btn_generate)
        self.layout_sidebar.addWidget(self.btn_view_d)
        self.layout_sidebar.addWidget(self.btn_messages)
        self.layout_sidebar.addWidget(self.btn_help)
        self.layout_sidebar.addStretch(1)

        self.p_start()

        self.panel_3 = QWidget(self)
        self.layout_3 = QVBoxLayout(self.panel_3)
        self.label3 = QLabel("Has seleccionado la opción 3", self.panel_3)
        self.layout_3.addWidget(self.label3)
        self.panel_3.setStyleSheet("background-color: #FFFFFF;")

        self.panel_4 = QWidget(self)
        self.layout_4 = QVBoxLayout(self.panel_4)
        self.label4 = QLabel("Has seleccionado la opción 4", self.panel_4)
        self.layout_4.addWidget(self.label4)
        self.panel_4.setStyleSheet("background-color: #000000;")

        self.p_dron()

        self.stack.addWidget(self.panel_right)
        self.stack.addWidget(self.panel_2)
        self.stack.addWidget(self.panel_3)
        self.stack.addWidget(self.panel_4)

        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.stack)

        self.layout_p.addWidget(self.splitter)
        self.setFixedSize(1000, 650)

    def p_start(self):
        # Panel
        self.panel_right = QWidget(self)
        self.layout_right = QVBoxLayout(self.panel_right)

        self.panel_up = QWidget(self.panel_right)
        self.layout_up = QVBoxLayout(self.panel_up)

        self.label1 = QLabel("Inicio", self.panel_up)
        self.label1.setStyleSheet("color:#ffffff")
        self.layout_up.addWidget(self.label1)
        self.panel_up.setFixedHeight(30)

        self.panel_init = QWidget(self.panel_right)
        self.layout_init = QHBoxLayout(self.panel_init)
        self.btn_init = self.big_buttons("Inicializari Sistema")
        self.btn_open = self.big_buttons("Cargar Archivo", self.show_dialog)
        self.btn_create = self.big_buttons("Generar Archivo")
        self.layout_init.addWidget(self.btn_init)
        self.layout_init.addWidget(self.btn_open)
        self.layout_init.addWidget(self.btn_create)
        # self.layout_init.addWidget(self.panel_init)
        self.panel_init.setStyleSheet("background-color: #202029")

        self.layout_right.addWidget(self.panel_up)
        self.layout_right.addWidget(self.panel_init)
        self.panel_right.setStyleSheet("background-color: #202029;")
        self.panel_right.setFixedHeight(320)

    def print_input(self):
        text = self.text_add.text()
        if text.strip():
            self.drone_list.insert_sorted(text)
            self.data_dron()
        else:
            error_msgbox("error", "Ingrese Datos para poder Ingresarlos")

    def change_view_dron(self):
        self.stack.setCurrentIndex(1)
        self.data_dron()

    def p_dron(self):
        self.panel_2 = QWidget(self)
        self.layout_2 = QVBoxLayout(self.panel_2)
        self.panel_add = QWidget(self.panel_2)
        self.layout_add = QHBoxLayout(self.panel_add)
        self.text_add = QLineEdit()
        self.text_add.setPlaceholderText("Escriba el nombre del Dron")
        self.text_add.setStyleSheet(
            """
    QLineEdit {
        border: 0px;
        border-radius: 4px;
        color:white;
        padding: 6px 8px;
        background: #332F40;
        selection-background-color: #3D384D;
    }
"""
        )
        self.btn_add = self.custom_button_form("Agregar", self.print_input)
        self.btn_add.setFixedSize(QtCore.QSize(120, 31))
        self.layout_add.addWidget(self.text_add)
        self.layout_add.addWidget(self.btn_add)
        self.panel_add.setFixedHeight(50)

        self.panel_table = QWidget(self.panel_2)
        self.layout_table = QVBoxLayout(self.panel_table)
        self.table = QTableWidget()
        # self.table.setRowCount(4)
        self.table.setColumnCount(1)

        self.header = self.table.horizontalHeader()
        self.header.setStyleSheet(
            "QHeaderView::section { background-color: #141519;color:#ffffff;border:0px;}"
        )
        self.header_vertical = self.table.verticalHeader()
        self.header_vertical.setStyleSheet(
            "QHeaderView::section { background-color: #141519;color:#ffffff;border:0px }"
        )
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Dron"))
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setStyleSheet(
            """
                QTableWidget {
                    background-color: #2a2a36;
                    gridline-color: #292a2f;
                    border:0px;
                    border-radius:10px;
                }
                QTableWidget::item {
                    color: #ffffff;
                }
                QTableWidget::item:selected {
                    background-color: #343442;
                }
                QTableCornerButton::section { background-color: #2a2a36 }
            """
        )
        self.layout_table.addWidget(self.table)
        self.layout_2.addWidget(self.panel_add)
        self.layout_2.addWidget(self.panel_table)

    def data_dron(self):
        current = self.drone_list.first
        i = 0
        self.table.setRowCount(0)
        while current:
            self.table.insertRow(self.table.rowCount())
            item = QTableWidgetItem(f"{current.i_d}")
            self.table.setItem(i, 0, item)
            i += 1
            current = current.next_node

    def custom_button(self, texto, funcion=None):
        boton = QPushButton(texto)
        boton.setStyleSheet(
            """
            QPushButton {
                background-color: #282833;
                color: #9d9da0;
                border: 0px;
                border-radius: 4px;
                padding:10px 0 8px 15px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #323240;
                color: #dcdcde;
            }
            QPushButton:pressed {
                background-color: #3C3C4D;
                color: #ffffff;
            }
        """
        )
        boton.clicked.connect(funcion)
        return boton

    def custom_button_form(self, texto, funcion=None):
        boton = QPushButton(texto)
        boton.setStyleSheet(
            """
            QPushButton {
                background-color: #73bcf6;
                color: #2a3343;
                border: 0px;
                font-weight:500;
                border-radius: 5px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #67A7DB;
                color: #2a3343;
            }
            QPushButton:pressed {
                background-color: #5B94C2;
                color: #202733;
            }
        """
        )
        boton.clicked.connect(funcion)
        return boton

    def big_buttons(self, texto, funcion=None):
        btn = QPushButton(texto)
        btn.setFixedSize(QtCore.QSize(220, 220))
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: #2F3340;
                color: #9EACD9;
                border: 0px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #383D4D;
                color: #A8B6E6;
            }
            QPushButton:pressed {
                background-color: #414759;
                color: #ffffff;
            }
        """
        )
        btn.clicked.connect(funcion)
        return btn

    def show_dialog(self):
        opciones = QFileDialog.Options()

        opciones |= QFileDialog.ReadOnly  # Opcional: Si solo deseas lectura

        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Archivo",
            "",
            "Archivos XML (*.xml);;Todos los Archivos (*)",
            options=opciones,
        )

        if archivo:
            read = Read()
            read.read_file(str(archivo))
            read.load_data(self.drone_list, self.s_list, self.m_list)
