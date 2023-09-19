import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from modules.readFiles import Read
from Tdas.linkedListD import LinkedListDrone


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drone_list = LinkedListDrone()
        # Crear un botón para abrir el cuadro de diálogo
        self.boton_abrir = QPushButton("Abrir Archivo", self)
        self.boton_abrir.clicked.connect(self.mostrar_dialogo)

        # Configurar la ventana principal
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Seleccionar Archivo")

    def mostrar_dialogo(self):
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
            print("Archivo seleccionado:", archivo)
            read = Read()
            read.read_file(str(archivo))
            read.load_data(self.drone_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
