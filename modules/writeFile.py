import xml.etree.ElementTree as ET
from xml.dom import minidom
from Tdas.linkedListD import LinkedListDrone


class Write:
    def __init__(self, route):
        self.route = route

    def write_document(self, data: LinkedListDrone):
        respuesta = ET.Element("respuesta")
        listadoMensajes = ET.SubElement(respuesta, "listaMensajes")
        current = data.first
        while current:
            current_matrix = current.value.rows.first
            rows = current_matrix.value.first
            times = current_matrix.value.size

            mensaje = ET.SubElement(listadoMensajes, "mensaje", nombre=f"{current.i_d}")
            sistemaDrones = ET.SubElement(mensaje, "sistemaDrones")
            sistemaDrones.text = f"{current.max_columns}"
            tiempoOptimo = ET.SubElement(mensaje, "tiempoOptimo")
            tiempoOptimo.text = f"{times}"
            mensajeRecibido = ET.SubElement(mensaje, "mensajeRecibido")
            mensajeRecibido.text = current.name_system
            instrucciones = ET.SubElement(mensaje, "instrucciones")

            for i in range(1, times + 1):
                tiempo = ET.SubElement(instrucciones, "tiempo", valor=f"{i}")
                acciones = ET.SubElement(tiempo, "acciones")
                temp = current.value.rows.first
                while temp:
                    columns = temp.value.first
                    for k in range(i - 1):
                        columns = columns.next_node
                    dron = ET.SubElement(
                        acciones, "dron", nombre=f"{temp.i_d}"
                    ).text = f"{columns.value}"
                    temp = temp.next_node
                # current_matrix = current.value.rows.first
                rows = rows.next_node
            current = current.next_node

        xmlstr = minidom.parseString(ET.tostring(respuesta)).toprettyxml(indent="   ")
        with open(self.route, "w", encoding="utf-8") as f:
            f.write(xmlstr)
