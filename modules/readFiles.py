import xml.etree.ElementTree as ET
from Tdas.linkedListD import LinkedList
from Tdas.doublyLinkedList import DoublyLinkedListSistem
from Tdas.mainS import MainSistem
from components.customMessage import *


class Read:
    def read_file(self, route):
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()

    def load_data(self, list_dron, list_sistem, list_messages):
        self.list_dron: LinkedList = list_dron
        self.list_sistem: LinkedList = list_sistem
        self.load_drones(list_dron)
        self.load_list_drone(list_sistem)
        self.load_list_mes(list_messages)
        # list_dron.print_drone()
        # list_sistem.print_temp()
        # list_messages.print_temp1()

    def load_drones(self, list_ori: LinkedList):
        for list_d in self.root.findall("listaDrones"):
            for dron in list_d.findall("dron"):
                list_ori.insert_sorted(dron.text)

    def load_list_drone(self, list_ori: LinkedList):
        for list_ in self.root.findall("listaSistemasDrones"):
            for sistem_l in list_.findall("sistemaDrones"):
                system_name = sistem_l.get("nombre")
                h_limit = sistem_l.findtext("alturaMaxima")
                d_limit = sistem_l.findtext("cantidadDrones")
                matrix = MainSistem(int(d_limit), int(h_limit))

                for content in sistem_l.findall("contenido"):
                    dron = content.findtext("dron")
                    temp = LinkedList()
                    if not self.list_dron.verify_dup(dron):
                        error_msgbox(
                            "Error",
                            f"El dron {dron} no esta en la lista de drones\nNo se agregará el sistema",
                        )
                        continue
                    for Hight in content.findall("alturas"):
                        for h in Hight.findall("altura"):
                            value = h.text
                            if int(h.get("valor")) <= int(h_limit):
                                if value is None:
                                    value = " "
                                temp.insert_sorted(h.get("valor"), value)
                    matrix.create_matrix(dron, temp)
                list_ori.insert_sorted(system_name, matrix)
                # print(matrix.rows, system_name)

    def load_list_mes(self, list_ori: LinkedList):
        for m_list in self.root.findall("listaMensajes"):
            for message in m_list.findall("Mensaje"):
                message_name = message.get("nombre")
                system_name = message.findtext("sistemaDrones")
                list_ins = DoublyLinkedListSistem()
                validate = self.list_sistem.verify_dup(system_name)
                # print(validate.value.col_limit)
                max_c = None
                if not validate:
                    error_msgbox(
                        "Error",
                        f"El Systema {system_name} no está registrado\nNo se agregará el sistema",
                    )
                    continue
                max_c = validate.value.col_limit

                for instructions in message.findall("instrucciones"):
                    for i in instructions.findall("instruccion"):
                        value = int(i.text)
                        dup = list_ins.search_from_end(i.get("dron"))
                        # dup = list_ins.search_from_end(i.get("dron"))

                        if not self.list_dron.verify_dup(i.get("dron")):
                            error_msgbox(
                                "Error",
                                f"El dron {i.get('dron')} no esta en la lista de drones\nNo se agregará el sistema",
                            )
                            continue

                        if int(i.text) > max_c:
                            error_msgbox(
                                "Error",
                                f"La altura {i.text} esta fuera de rango\nLimite: {max_c}\nSistema de dron: {system_name}",
                            )
                            continue

                        if dup:
                            value -= dup.h_inst

                        list_ins.insert(i.get("dron"), value, int(i.text))
                list_ori.insert_sorted_msg(
                    message_name, list_ins, system_name, validate.value.row_limit
                )
