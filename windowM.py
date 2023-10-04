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
from components.styles import Styles


class WindowP(QWidget):
    def __init__(self):
        super().__init__()
        self.drone_list = LinkedList()
        self.s_list = LinkedList()
        self.m_list = LinkedList()
        self.inst_list = LinkedList()
        self.processed = LinkedList()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Proyecto 2")
        self.setStyleSheet("background-color: #171821;")
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

        self.btn_generate = self.custom_button(
            "  Inicio", QIcon(Icons.BTN_HOME_HOVER), self.change_view_init
        )
        self.btn_view_d = self.custom_button(
            "  Drones", QIcon(Icons.BTN_DRON), self.change_view_dron
        )
        self.btn_messages = self.custom_button(
            "  Mensajes", QIcon(Icons.BTN_MESSAGE), self.change_view_m
        )
        self.btn_help = self.custom_button(
            "  Ayuda", QIcon(Icons.BTN_INFO), self.change_view_help
        )

        self.layout_sidebar.addWidget(self.btn_generate)
        self.layout_sidebar.addWidget(self.btn_view_d)
        self.layout_sidebar.addWidget(self.btn_messages)
        self.layout_sidebar.addWidget(self.btn_help)
        self.layout_sidebar.addStretch(1)

        self.btn_generate.setStyleSheet(Styles.SIDEBAR_BTN_ACTIVE)

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
        self.layout_right.setContentsMargins(20, 20, 20, 20)

        panel_prin = QWidget(self.panel_right)
        layout_prin = QVBoxLayout(panel_prin)
        # panel_prin.setStyleSheet("background-color:#21222d; border-radius:10px")

        self.panel_up = QWidget(panel_prin)
        self.layout_up = QVBoxLayout(self.panel_up)

        self.label1 = QLabel("Inicio")
        self.label1.setStyleSheet("color:#ffffff;font-weight:500;")
        self.layout_up.addWidget(self.label1)
        self.panel_up.setFixedHeight(30)

        self.panel_init = QWidget(panel_prin)
        self.layout_init = QHBoxLayout(self.panel_init)
        icon_init = QtGui.QIcon(Icons.BTN_RESET)
        icon_upload = QtGui.QIcon(Icons.BTN_UPL)
        icon_xml = QtGui.QIcon(Icons.BTN_XML)
        icon_prcess = QtGui.QIcon(Icons.BTN_PROCESS)

        self.btn_open = self.big_buttons(
            "Cargar Archivo", icon_upload, self.show_dialog
        )
        self.btn_create = self.big_buttons("Generar Archivo", icon_xml, self.create_xml)

        # self.layout_init.addWidget(self.btn_init)
        self.layout_init.addWidget(self.btn_open)
        self.layout_init.addWidget(self.btn_create)

        self.panel_second = QWidget(panel_prin)
        self.layout_second = QHBoxLayout(self.panel_second)

        self.btn_process = self.big_buttons(
            "Procesar Datos", icon_prcess, self.process_file
        )
        self.btn_init = self.big_buttons("Inicializar Sistema", icon_init, self.reset)
        self.layout_second.addWidget(self.btn_process)
        self.layout_second.addWidget(self.btn_init)
        # self.layout_init.addWidget(self.panel_init)
        # self.panel_init.setStyleSheet("background-color: #171821")

        # self.layout_right.addWidget(self.panel_up)
        # self.layout_right.addWidget(self.panel_init)
        # self.layout_right.addWidget(self.panel_second)
        layout_prin.addWidget(self.panel_up)
        layout_prin.addWidget(self.panel_init)
        layout_prin.addWidget(self.panel_second)
        self.layout_right.addWidget(panel_prin)
        self.panel_right.setStyleSheet("background-color: #171821;")
        # self.panel_right.setFixedHeight(520)

    def print_input(self):
        text = self.text_add.text()
        if text.strip():
            size = self.drone_list.size
            self.drone_list.insert_sorted(text, is_dron=True)
            self.data_dron()
            if size < self.drone_list.size:
                correct_msgbox("Operación Exitosa", "Dron registrado correctamente")
                self.text_add.setText("")
        else:
            error_msgbox("error", "Ingrese Datos para poder Ingresarlos")

    def change_view_init(self):
        self.stack.setCurrentIndex(0)
        self.reset_button_colors()
        self.btn_generate.setStyleSheet(Styles.SIDEBAR_BTN_ACTIVE)
        self.btn_generate.setIcon(QIcon(Icons.BTN_HOME_HOVER))

    def change_view_dron(self):
        self.stack.setCurrentIndex(1)
        self.reset_button_colors()
        self.btn_view_d.setStyleSheet(Styles.SIDEBAR_BTN_ACTIVE)
        self.btn_view_d.setIcon(QIcon(Icons.BTN_DRON_HOVER))
        self.data_dron()

    def change_view_m(self):
        self.stack.setCurrentIndex(2)
        self.reset_button_colors()
        self.btn_messages.setStyleSheet(Styles.SIDEBAR_BTN_ACTIVE)
        self.btn_messages.setIcon(QIcon(Icons.BTN_MESSAGE_HOVER))
        self.data_messages()

    def change_view_help(self):
        self.stack.setCurrentIndex(3)
        self.reset_button_colors()
        self.btn_help.setStyleSheet(Styles.SIDEBAR_BTN_ACTIVE)
        self.btn_help.setIcon(QIcon(Icons.BTN_INFO_HOVER))

    def p_dron(self):
        self.panel_2 = QWidget(self)
        self.layout_2 = QVBoxLayout(self.panel_2)
        label_add = QLabel("  Agregar un Dron")
        label_add.setStyleSheet("color:white;font-weight:500")
        self.layout_2.addWidget(label_add)
        self.layout_2.setSpacing(0)
        self.panel_add = QWidget(self.panel_2)
        self.layout_add = QHBoxLayout(self.panel_add)
        self.text_add = QLineEdit()
        self.text_add.setPlaceholderText("Escriba el nombre del Dron")
        self.text_add.setStyleSheet(Styles.INPUT_DRON)
        self.btn_add = self.custom_button_form("Agregar", self.print_input)
        self.btn_add.setFixedSize(QtCore.QSize(120, 31))
        self.layout_add.addWidget(self.text_add)
        self.layout_add.addWidget(self.btn_add)
        self.panel_add.setFixedHeight(50)

        self.panel_title_t = QWidget(self.panel_2)
        self.layout_title_t = QHBoxLayout(self.panel_title_t)
        self.label_title1 = QLabel("Listado de Drones")
        self.label_title1.setStyleSheet("color:#ffffff;font-weight:500;")
        self.layout_title_t.addWidget(self.label_title1)
        self.panel_title_t.setFixedHeight(32)

        self.panel_table = QWidget(self.panel_2)
        self.layout_table = QVBoxLayout(self.panel_table)
        self.table = QTableWidget()
        # self.table.setRowCount(4)
        self.table.setColumnCount(1)

        self.header = self.table.horizontalHeader()
        self.header.setStyleSheet(Styles.HEADER_TABLE)
        self.header_vertical = self.table.verticalHeader()
        self.header_vertical.setStyleSheet(
            "QHeaderView::section { background-color: #171821;color:#ffffff;border:0px }"
        )
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setStyleSheet(Styles.S_SCROLLBAR_TABLE)

        self.layout_table.addWidget(self.table)

        self.panel_system = QWidget(self.panel_2)
        self.layout_system = QVBoxLayout(self.panel_system)

        self.lable_system = QLabel("Sistema de Drones")
        self.lable_system.setStyleSheet("color:#ffffff;font-weight:500;")
        self.lable_system.setStyleSheet("color:white")
        self.btn_graph_system = QPushButton("Graficar")
        self.btn_graph_system.setStyleSheet(Styles.BLUE_BTN)
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
        self.panel_3.setStyleSheet("background-color: #171821;")
        panel_message = QWidget(self.panel_3)
        layout_message = QVBoxLayout(panel_message)
        label_mesages = QLabel("Listado de Mensajes")
        label_mesages.setStyleSheet("color:#ffffff;font-weight:500;")
        label_mesages.setStyleSheet("color:white")
        self.table_messages = QTableWidget()
        self.table_messages.setColumnCount(2)
        self.table_messages.setHorizontalHeaderItem(0, QTableWidgetItem("Nombre"))
        self.table_messages.setHorizontalHeaderItem(
            1, QTableWidgetItem("Instrucciones")
        )
        header_messages = self.table_messages.horizontalHeader()
        header_messages.setStyleSheet(Styles.HEADER_TABLE)
        header_v = self.table_messages.verticalHeader()
        header_v.setStyleSheet(
            "QHeaderView::section { background-color: #171821;color:#ffffff;border:0px }"
        )
        header_messages.setSectionResizeMode(QHeaderView.Stretch)

        layout_message.addWidget(label_mesages)
        self.table_messages.setStyleSheet(Styles.S_SCROLLBAR_TABLE)
        layout_message.addWidget(self.table_messages)

        panel_instructions = QWidget(self.panel_3)
        layout_instructions = QVBoxLayout(panel_instructions)

        label_instructins = QLabel("Instrucciones a Enviar")
        label_instructins.setStyleSheet("color:#ffffff;font-weight:500;")
        layout_instructions.addWidget(label_instructins)

        panel_data = QWidget(panel_instructions)
        layout_data = QHBoxLayout(panel_data)
        layout_data.setContentsMargins(0, 0, 0, 0)
        self.combo = QComboBox()
        self.combo.setStyleSheet(Styles.S_COMBOBOX)
        btn_data = QPushButton("Ver Información")
        btn_data.setStyleSheet(Styles.PURPLE_BTN)
        btn_data.clicked.connect(self.view_information)
        btn_graph = QPushButton("Gráficar")
        btn_graph.setStyleSheet(Styles.BLUE_BTN)
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

        self.layout_4.setContentsMargins(20, 15, 20, 10)
        self.panel_4.setFixedHeight(300)
        panel_data = QWidget(self.panel_4)
        layout_data = QVBoxLayout(panel_data)
        panel_data.setStyleSheet("background-color:#21222d; border-radius:10px")
        label_title = QLabel("Datos del Estudiante")
        label_title.setStyleSheet("color:white;font-weight:700")
        # panel_data.setFixedHeight(200)

        panel_prin = QWidget(panel_data)
        layout_prin = QVBoxLayout(panel_prin)
        layout_prin.setContentsMargins(5, 5, 5, 5)
        label_img = QLabel("Joab Israel Ajsivinac Ajsivinac")
        label_img.setStyleSheet("color:white")
        label_cl = QLabel('Introducción a la Programación y computación 2 sección "N"')
        label_cl.setStyleSheet("color:white")
        layout_prin.addWidget(label_img)

        panel_info = QWidget(panel_prin)
        layout_info = QHBoxLayout(panel_info)

        panel_data5 = QWidget(panel_info)
        layout_data5 = QVBoxLayout(panel_data5)
        label_t1 = QLabel("Carné")
        label_t1.setStyleSheet("color:#ffffff;font-weight:500;")
        label_c = QLabel("202200135")
        label_c.setStyleSheet("color:white")
        layout_data5.addWidget(label_t1)
        layout_data5.addWidget(label_c)

        panel_data1 = QWidget(panel_info)
        layout_data1 = QVBoxLayout(panel_data1)
        label_t2 = QLabel("Carrera")
        label_t2.setStyleSheet("color:#ffffff;font-weight:500;")
        label_c2 = QLabel("Ingeniería en Ciencias y Sistemas")
        label_c2.setStyleSheet("color:white")
        layout_data1.addWidget(label_t2)
        layout_data1.addWidget(label_c2)

        panel_data2 = QWidget(panel_info)
        layout_data2 = QVBoxLayout(panel_data2)
        label_t3 = QLabel("Semestre")
        label_t3.setStyleSheet("color:#ffffff;font-weight:500;")
        label_c3 = QLabel("Cuarto")
        label_c3.setStyleSheet("color:white")
        layout_data2.addWidget(label_t3)
        layout_data2.addWidget(label_c3)

        layout_data.addWidget(label_title)
        layout_data.addWidget(panel_prin)

        panel_btn1 = QWidget(panel_data)
        layout_btn1 = QVBoxLayout(panel_btn1)
        btn_doc = QPushButton("Ver Documentación")
        btn_doc.setStyleSheet(Styles.BLUE_BTN)
        btn_doc.clicked.connect(self.view_doc)
        # layout_btn1.addWidget(label_text1)
        layout_btn1.addWidget(btn_doc)
        layout_data.addWidget(panel_btn1)

        layout_prin.addWidget(panel_info)

        layout_info.addWidget(panel_data5)
        layout_info.addWidget(panel_data1)
        layout_info.addWidget(panel_data2)
        layout_prin.addWidget(label_cl)
        self.panel_4.setStyleSheet("background-color: #171821;")
        self.layout_4.addWidget(panel_data)

    def data_dron(self):
        current = self.drone_list.first
        i = 0
        self.table.setRowCount(0)
        while current:
            self.table.insertRow(self.table.rowCount())
            self.table.setRowHeight(i, 40)
            item = QTableWidgetItem(f"{current.i_d}")
            self.table.setItem(i, 0, item)
            i += 1
            current = current.next_node

    def data_messages(self):
        current = self.processed.first
        current_inst = self.m_list.first
        # print(self.processed.size)
        # print(self.m_list.size)
        i = 0
        self.table_messages.setRowCount(0)
        self.combo.clear()
        while current:
            self.table_messages.insertRow(self.table_messages.rowCount())
            self.table_messages.setRowHeight(i, 85)
            for j in range(2):
                item = None
                if j == 0:
                    item = QTableWidgetItem(f"{current.i_d}")
                    self.combo.addItem(f"{current.i_d}")
                elif j == 1:
                    item = QTextEdit()
                    item.setStyleSheet(Styles.TEXT_INSTRUCTIONS)
                    current_v = current_inst.value.first
                    while current_v:
                        item.append(f"{current_v.i_d},{current_v.h_inst}")
                        current_v = current_v.next_node
                    item.setReadOnly(True)
                    self.table_messages.setCellWidget(i, j, item)
                    continue
                self.table_messages.setItem(i, j, item)
            # print(current.i_d, current.value, current.name_system, current_inst.value)
            i += 1
            current = current.next_node
            current_inst = current_inst.next_node

    def reset_button_colors(self):
        self.btn_generate.setStyleSheet(Styles.SIDEBAR_BTN)
        self.btn_generate.setIcon(QIcon(Icons.BTN_HOME))
        self.btn_view_d.setStyleSheet(Styles.SIDEBAR_BTN)
        self.btn_view_d.setIcon(QIcon(Icons.BTN_DRON))
        self.btn_messages.setStyleSheet(Styles.SIDEBAR_BTN)
        self.btn_messages.setIcon(QIcon(Icons.BTN_MESSAGE))
        self.btn_help.setStyleSheet(Styles.SIDEBAR_BTN)
        self.btn_help.setIcon(QIcon(Icons.BTN_INFO))

    def custom_button(self, texto, icon, funcion=None):
        btn = QPushButton(texto)
        btn.setStyleSheet(Styles.SIDEBAR_BTN)
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(22, 22))
        btn.clicked.connect(funcion)
        return btn

    def custom_button_form(self, texto, funcion=None):
        boton = QPushButton(texto)
        boton.setStyleSheet(Styles.FORM_BTN)
        boton.clicked.connect(funcion)
        return boton

    def big_buttons(self, texto, icon, funcion=None):
        btn = QToolButton()
        btn.setText(texto)
        btn.setFixedSize(QtCore.QSize(220, 220))
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(135, 135))
        btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btn.setStyleSheet(Styles.PRINC_BTN)
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
            correct_msgbox("Carga Completada", "Los datos válidos se han registrado")

    def process_file(self):
        if self.m_list.size == 0:
            alert_msgbox("Advertencia", "No hay datos Cargados")
            return
        self.m_list.call_optimize(self.s_list, self.processed)
        correct_msgbox(
            "Procesamiento Completado", "Los datos válidos se han registrado"
        )

    def reset(self):
        self.drone_list.empty_list()
        self.s_list.empty_list()
        self.m_list.empty_list()
        self.inst_list.empty_list()
        self.processed.empty_list()
        correct_msgbox("Operación Exitosa", "El sistema se Inicializo")

    def create_xml(self):
        if self.processed.size == 0:
            alert_msgbox("Advertencia", "No hay datos Procesados")
            return
        w = Write("salida.xml")
        w.write_document(self.processed)
        correct_msgbox("Operación Exitosa", "Archivo creado correctamente")

    def graph_system(self):
        if self.s_list.size == 0:
            alert_msgbox("Advertencia", "No hay datos Cargados")
            return
        gr = Graph("grafica_sistemas")
        gr.create_sistem(self.s_list)

    def view_information(self):
        if self.processed.size == 0:
            alert_msgbox("Advertencia", "No hay datos Cargados")
            return
        text = self.combo.currentText()
        found = self.processed.s_search_b_hight(text)
        information_msgbox(
            "Información",
            found.max_columns,
            found.name_system,
            f"{found.value.rows.first.value.size}",
        )

    def graph_instructions(self):
        if self.processed.size == 0:
            alert_msgbox("Advertencia", "No hay datos Cargados")
            return
        text = self.combo.currentText()
        found = self.processed.s_search_b_hight(text)
        if found is None:
            error_msgbox("Error", "No hay instrucciones para el mensaje")
            return
        gr = Graph(f"grafica_{found.i_d}")
        gr.create_message(found)

    def view_doc(self):
        webbrowser.open(
            "https://github.com/J-Ajsivinac/IPC2_Proyecto2_202200135/blob/main/Doc/Documentacion_202200135.pdf"
        )
