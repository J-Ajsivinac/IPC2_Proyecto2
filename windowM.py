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
    QTextEdit,
    QComboBox,
    QToolButton,
)
from PySide6.QtGui import QFont
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
import sys
from modules.readFiles import Read
from modules.writeFile import Write
from Tdas.linkedListD import LinkedList
from components.customMessage import *
from modules.graph import Graph
import webbrowser
from icons.iconos import Icons


class WindowP(QWidget):
    def __init__(self):
        super().__init__()
        self.drone_list = LinkedList()
        self.s_list = LinkedList()
        self.m_list = LinkedList()
        self.inst_list = LinkedList()
        self.processed = LinkedList()
        self.sidebar_active = """ QPushButton {
                background-color: #242833;
                color: #b1b8fa;
                border: 0px;
                border-radius: 4px;
                padding:12px 0 12px 15px;
                text-align: left;
            }"""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Proyecto 2")
        self.setStyleSheet(f"background-color: #171821;")
        self.layout_p = QVBoxLayout(self)
        self.layout_p.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self)
        self.stack = QStackedWidget(self)

        # Sidebar
        self.sidebar = QWidget(self)
        self.layout_sidebar = QVBoxLayout(self.sidebar)
        self.layout_sidebar.setContentsMargins(10, 208, 10, 10)
        self.sidebar.setStyleSheet("background-color: #13151b;")
        self.sidebar.setFixedWidth(220)
        self.layout_sidebar.setSpacing(20)

        self.btn_generate = self.custom_button("Inicio", self.change_view_init)
        self.btn_view_d = self.custom_button("Drones", self.change_view_dron)
        # self.btn_view_list = self.custom_button("Sistemas de Drones")
        self.btn_messages = self.custom_button("Mensajes", self.change_view_m)
        self.btn_help = self.custom_button("Ayuda", self.change_view_help)
        self.layout_sidebar.addWidget(self.btn_generate)
        self.layout_sidebar.addWidget(self.btn_view_d)
        self.layout_sidebar.addWidget(self.btn_messages)
        self.layout_sidebar.addWidget(self.btn_help)
        self.layout_sidebar.addStretch(1)

        self.btn_generate.setStyleSheet(self.sidebar_active)

        self.p_start()
        self.p_help()

        self.p_dron()
        self.p_message()
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
        icon_init = QtGui.QIcon(Icons.BTN_RESET)
        icon_upload = QtGui.QIcon(Icons.BTN_UPL)
        icon_xml = QtGui.QIcon(Icons.BTN_XML)
        self.btn_init = self.big_buttons("Inicializari Sistema", icon_init)

        self.btn_open = self.big_buttons(
            "Cargar Archivo", icon_upload, self.show_dialog
        )
        self.btn_create = self.big_buttons("Generar Archivo", icon_xml, self.create_xml)
        self.layout_init.addWidget(self.btn_init)
        self.layout_init.addWidget(self.btn_open)
        self.layout_init.addWidget(self.btn_create)
        # self.layout_init.addWidget(self.panel_init)
        self.panel_init.setStyleSheet("background-color: #171821")

        self.layout_right.addWidget(self.panel_up)
        self.layout_right.addWidget(self.panel_init)
        self.panel_right.setStyleSheet("background-color: #171821;")
        self.panel_right.setFixedHeight(320)

    def print_input(self):
        text = self.text_add.text()
        if text.strip():
            self.drone_list.insert_sorted(text)
            self.data_dron()
        else:
            error_msgbox("error", "Ingrese Datos para poder Ingresarlos")

    def change_view_init(self):
        self.stack.setCurrentIndex(0)
        self.reset_button_colors()
        self.btn_generate.setStyleSheet(self.sidebar_active)

    def change_view_dron(self):
        self.stack.setCurrentIndex(1)
        self.reset_button_colors()
        self.btn_view_d.setStyleSheet(self.sidebar_active)
        self.data_dron()

    def change_view_m(self):
        self.stack.setCurrentIndex(2)
        self.reset_button_colors()
        self.btn_messages.setStyleSheet(self.sidebar_active)
        self.data_messages()

    def change_view_help(self):
        self.stack.setCurrentIndex(3)
        self.reset_button_colors()
        self.btn_help.setStyleSheet(self.sidebar_active)

    def p_dron(self):
        self.panel_2 = QWidget(self)
        self.layout_2 = QVBoxLayout(self.panel_2)
        self.layout_2.setSpacing(0)
        self.panel_add = QWidget(self.panel_2)
        self.layout_add = QHBoxLayout(self.panel_add)
        self.text_add = QLineEdit()
        self.text_add.setPlaceholderText("Escriba el nombre del nuevo Dron")
        self.text_add.setStyleSheet(
            """
    QLineEdit {
        border: 0px;
        border-radius: 4px;
        color:white;
        padding: 6px 8px;
        background: #252633;
        selection-background-color: #595C7A;
    }
"""
        )
        self.btn_add = self.custom_button_form("Agregar", self.print_input)
        self.btn_add.setFixedSize(QtCore.QSize(120, 31))
        self.layout_add.addWidget(self.text_add)
        self.layout_add.addWidget(self.btn_add)
        self.panel_add.setFixedHeight(50)

        self.panel_title_t = QWidget(self.panel_2)
        self.layout_title_t = QHBoxLayout(self.panel_title_t)
        self.label_title1 = QLabel("Listado de Drones")
        self.label_title1.setStyleSheet("QLabel { color:#ffffff; padding:0 }")
        self.layout_title_t.addWidget(self.label_title1)
        self.panel_title_t.setFixedHeight(32)

        self.panel_table = QWidget(self.panel_2)
        self.layout_table = QVBoxLayout(self.panel_table)
        self.table = QTableWidget()
        # self.table.setRowCount(4)
        self.table.setColumnCount(1)

        self.header = self.table.horizontalHeader()
        self.header.setStyleSheet(
            """
            QHeaderView::section 
            { 
                background-color: #141519;
                color:#ffffff;border:0px;
                border-top-left-radius:10px;
                border-top-right-radius:10px;
            }"""
        )
        self.header_vertical = self.table.verticalHeader()
        self.header_vertical.setStyleSheet(
            "QHeaderView::section { background-color: #141519;color:#ffffff;border:0px }"
        )
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
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

        self.panel_system = QWidget(self.panel_2)
        self.layout_system = QVBoxLayout(self.panel_system)

        self.lable_system = QLabel("Sistema de Drones")
        self.btn_graph_system = QPushButton("Graficar")
        self.btn_graph_system.clicked.connect(self.graph_system)
        self.layout_system.addWidget(self.lable_system)
        self.layout_system.addWidget(self.btn_graph_system)

        self.layout_2.addWidget(self.panel_add)
        self.layout_2.addWidget(self.panel_title_t)
        self.layout_2.addWidget(self.panel_table)
        self.layout_2.addWidget(self.panel_system)

    def p_message(self):
        self.panel_3 = QWidget(self)
        self.layout_3 = QVBoxLayout(self.panel_3)
        self.panel_3.setStyleSheet("background-color: #202029;")
        panel_message = QWidget(self.panel_3)
        layout_message = QVBoxLayout(panel_message)
        label_mesages = QLabel("Listado de Mensajes")
        self.table_messages = QTableWidget()
        self.table_messages.setColumnCount(2)
        self.table_messages.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
        self.table_messages.setHorizontalHeaderItem(
            1, QTableWidgetItem("Instrucciones")
        )
        header_messages = self.table_messages.horizontalHeader()
        header_messages.setSectionResizeMode(QHeaderView.Stretch)

        layout_message.addWidget(label_mesages)
        self.table_messages.setStyleSheet(
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
        layout_message.addWidget(self.table_messages)

        panel_instructions = QWidget(self.panel_3)
        layout_instructions = QVBoxLayout(panel_instructions)
        label_instructins = QLabel("Instrucciones a Enviar")
        layout_instructions.addWidget(label_instructins)

        panel_data = QWidget(panel_instructions)
        layout_data = QHBoxLayout(panel_data)
        self.combo = QComboBox()
        self.combo.setStyleSheet(
            """
    QComboBox {
        background-color: #272727;
        color: #ffffff;
    }
"""
        )
        btn_data = QPushButton("Ver Información")
        btn_data.clicked.connect(self.view_information)
        btn_graph = QPushButton("Gráficar")
        btn_graph.clicked.connect(self.graph_instructions)
        layout_data.addWidget(self.combo)
        layout_data.addWidget(btn_data)
        layout_data.addWidget(btn_graph)
        layout_instructions.addWidget(panel_data)

        self.layout_3.addWidget(panel_message)
        self.layout_3.addWidget(panel_instructions)

    def p_help(self):
        self.panel_4 = QWidget(self)
        self.layout_4 = QVBoxLayout(self.panel_4)
        self.panel_4.setFixedHeight(200)
        panel_data = QWidget(self.panel_4)
        layout_data = QVBoxLayout(panel_data)

        label_title = QLabel("Datos del Estudiante")
        # panel_data.setFixedHeight(200)

        panel_prin = QWidget(panel_data)
        layout_prin = QVBoxLayout(panel_prin)
        layout_prin.setContentsMargins(0, 0, 0, 0)
        label_img = QLabel("Joab Israel Ajsivinac Ajsivinac")
        label_cl = QLabel('Introducción a la Programación y computación 2 sección "N"')
        layout_prin.addWidget(label_img)

        panel_info = QWidget(panel_prin)
        layout_info = QHBoxLayout(panel_info)

        panel_data5 = QWidget(panel_info)
        layout_data5 = QVBoxLayout(panel_data5)
        label_t1 = QLabel("Carné")
        label_c = QLabel("202200135")
        layout_data5.addWidget(label_t1)
        layout_data5.addWidget(label_c)

        panel_data1 = QWidget(panel_info)
        layout_data1 = QVBoxLayout(panel_data1)
        label_t2 = QLabel("Carrera")
        label_c2 = QLabel("Ingeniería en Ciencias y Sistemas")
        layout_data1.addWidget(label_t2)
        layout_data1.addWidget(label_c2)

        panel_data2 = QWidget(panel_info)
        layout_data2 = QVBoxLayout(panel_data2)
        label_t3 = QLabel("Semestre")
        label_c3 = QLabel("Cuarto")
        layout_data2.addWidget(label_t3)
        layout_data2.addWidget(label_c3)

        layout_data.addWidget(label_title)
        layout_data.addWidget(panel_prin)

        panel_btn1 = QWidget(panel_data)
        layout_btn1 = QVBoxLayout(panel_btn1)
        label_text1 = QLabel("Ayuda")
        btn_doc = QPushButton("Ver Documentación")
        btn_doc.clicked.connect(self.view_doc)
        layout_btn1.addWidget(label_text1)
        layout_btn1.addWidget(btn_doc)
        layout_data.addWidget(panel_btn1)

        layout_prin.addWidget(panel_info)

        layout_info.addWidget(panel_data5)
        layout_info.addWidget(panel_data1)
        layout_info.addWidget(panel_data2)
        layout_prin.addWidget(label_cl)
        self.panel_4.setStyleSheet("background-color: #2a2a36;")
        self.layout_4.addWidget(panel_data)

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

    def data_messages(self):
        current = self.processed.first
        current_inst = self.m_list.first
        i = 0
        self.table_messages.setRowCount(0)
        while current:
            self.table_messages.insertRow(self.table_messages.rowCount())
            self.table_messages.setRowHeight(i, 80)
            for j in range(2):
                item = None
                if j == 0:
                    item = QTableWidgetItem(f"{current.i_d}")
                    self.combo.addItem(f"{current.i_d}")
                elif j == 1:
                    item = QTextEdit()
                    current_v = current_inst.value.first
                    while current_v:
                        item.append(f"{current_v.i_d},{current_v.h_inst}")
                        current_v = current_v.next_node
                    self.table_messages.setCellWidget(i, j, item)
                    continue
                self.table_messages.setItem(i, j, item)
            # print(current.i_d, current.value, current.name_system, current_inst.value)
            i += 1
            current = current.next_node
            current_inst = current_inst.next_node

    def reset_button_colors(self):
        style = """
            QPushButton {
                background-color: #13151b;
                color: #696a78;
                border: 0px;
                border-radius: 4px;
                padding:12px 0 12px 15px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #1B1E26;
                color: #dcdcde;
            }
        """
        self.btn_generate.setStyleSheet(style)
        self.btn_view_d.setStyleSheet(style)
        self.btn_messages.setStyleSheet(style)
        self.btn_help.setStyleSheet(style)

    def custom_button(self, texto, funcion=None):
        boton = QPushButton(texto)
        boton.setStyleSheet(
            """
            QPushButton {
                background-color: #13151b;
                color: #696a78;
                border: 0px;
                border-radius: 4px;
                padding:12px 0 12px 15px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #1B1E26;
                color: #dcdcde;
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
                background-color: #a6f1c8;
                color: #000002;
                border: 0px;
                font-weight:500;
                border-radius: 5px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #9BE1BB;
                color: #2a3343;
            }
            QPushButton:pressed {
                background-color: #89C7A5;
                color: #202733;
            }
        """
        )
        boton.clicked.connect(funcion)
        return boton

    def big_buttons(self, texto, icon, funcion=None):
        btn = QToolButton()
        btn.setText(texto)
        btn.setFixedSize(QtCore.QSize(220, 220))
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(135, 135))
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn.setStyleSheet(
            """
            QToolButton {
                background-color: #2B2C3B;
                color: #636587;
                border: 0px;
                font-weight:600;
                border-radius: 6px;
            }
            QToolButton:hover {
                background-color: #303242;
                color: #9195C7;
            }
            QToolButton:pressed {
                background-color: #343547;
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
            self.m_list.call_optimize(self.s_list, self.processed)
            # self.processed.print_temp()

    def create_xml(self):
        w = Write("salida.xml")
        w.write_document(self.processed)

    def graph_system(self):
        gr = Graph("grafica_sistemas")
        gr.create_sistem(self.s_list)

    def view_information(self):
        text = self.combo.currentText()
        found = self.processed.s_search_b_hight(text)
        information_msgbox(
            "Información",
            found.max_columns,
            found.name_system,
            f"{found.value.rows.first.value.size}",
        )
        # print(
        #     "Información",
        #     found.max_columns,
        #     found.name_system,
        #     found.value.rows.first.value.size,
        # )

    def graph_instructions(self):
        text = self.combo.currentText()
        found = self.processed.s_search_b_hight(text)
        gr = Graph(f"grafica_{found.i_d}")
        gr.create_message(found)

    def view_doc(self):
        webbrowser.open(
            "https://github.com/J-Ajsivinac/IPC2_Proyecto2_202200135/tree/main/Doc"
        )
