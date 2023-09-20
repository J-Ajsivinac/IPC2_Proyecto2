from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QLabel,
    QWidget,
    QSplitter,
    QStackedWidget,
    QFileDialog,
)
from PySide6.QtGui import QFont
import sys
from modules.readFiles import Read
from Tdas.linkedListD import LinkedListDrone


class WindowP(QWidget):
    def __init__(self):
        super().__init__()
        self.drone_list = LinkedListDrone()
        self.s_list = LinkedListDrone()
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
        self.layout_sidebar.setContentsMargins(10, 20, 10, 10)
        self.sidebar.setStyleSheet("background-color: #1c1c24;")
        self.sidebar.setFixedWidth(220)
        self.layout_sidebar.setSpacing(10)

        # Botones
        self.btn_init = self.custom_button("Inicializar", self.show_dialog)
        # self.btn_init.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.layout_sidebar.addWidget(self.btn_init)

        self.btn_load = self.custom_button(
            "Cargar Archivo", lambda: self.stack.setCurrentIndex(1)
        )
        # self.btn_load.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.layout_sidebar.addWidget(self.btn_load)

        self.btn_generate = self.custom_button("Generar Archivo")
        self.btn_view_d = self.custom_button("Drones")
        self.btn_view_list = self.custom_button("Sistemas de Drones")
        self.btn_messages = self.custom_button("Mensajes")
        self.btn_help = self.custom_button("Ayuda")
        self.layout_sidebar.addWidget(self.btn_generate)
        self.layout_sidebar.addWidget(self.btn_view_d)
        self.layout_sidebar.addWidget(self.btn_view_list)
        self.layout_sidebar.addWidget(self.btn_messages)
        self.layout_sidebar.addWidget(self.btn_help)
        self.layout_sidebar.addStretch(1)

        # Panel
        self.panel_right = QWidget(self)
        self.layout_right = QVBoxLayout(self.panel_right)
        self.label1 = QLabel("Has seleccionado la opción 1", self.panel_right)
        self.layout_right.addWidget(self.label1)
        self.panel_right.setStyleSheet("background-color: #202029;")

        self.panel_2 = QWidget(self)
        self.layout_2 = QVBoxLayout(self.panel_2)
        self.label2 = QLabel("Has seleccionado la opción 2", self.panel_2)
        self.layout_2.addWidget(self.label2)
        self.panel_2.setStyleSheet("background-color: #FFB6C1;")  # Color rosa claro

        self.stack.addWidget(self.panel_right)
        self.stack.addWidget(self.panel_2)

        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.stack)

        self.layout_p.addWidget(self.splitter)
        self.setFixedSize(1000, 650)

    def custom_button(self, texto, funcion=None):
        boton = QPushButton(texto)
        boton.setStyleSheet(
            """
            QPushButton {
                background-color: #282833;
                color: #9d9da0;
                border: 0px;
                border-radius: 4px;
                padding:10px 0 8px 0;
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
            read.load_data(self.drone_list, self.s_list)
