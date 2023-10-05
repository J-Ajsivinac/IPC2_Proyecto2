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

    def load_drones(self, list_ori: LinkedList):
        for list_d in self.root.findall("listaDrones"):
            for dron in list_d.findall("dron"):
                list_ori.insert_sorted(dron.text, is_dron=True)

    def load_list_drone(self, list_ori: LinkedList):
        for list_ in self.root.findall("listaSistemasDrones"):
            for sistem_l in list_.findall("sistemaDrones"):
                system_name = sistem_l.get("nombre")
                h_limit = sistem_l.findtext("alturaMaxima")
                d_limit = sistem_l.findtext("cantidadDrones")
                if int(h_limit) > 100:
                    alert_msgbox(
                        "Advertencia",
                        f"Limite de alturas sobrepasado\nSistema de drones: {h_limit}",
                    )
                if int(d_limit) > 200:
                    alert_msgbox(
                        "Advertencia",
                        f"El limite de drones sobrepasado\nSistema de drones: {h_limit}",
                    )
                matrix = MainSistem(int(d_limit), int(h_limit))
                error = False
                update_row = False
                update_all = False
                for content in sistem_l.findall("contenido"):
                    if error:
                        continue
                    dron = content.findtext("dron")
                    temp = LinkedList()
                    temp_list = self.list_sistem.verify_dup(system_name)
                    if temp_list:
                        matrix = temp_list.value
                        update_all = True
                        # print(matrix.rows.size, matrix.row_limit, "---")

                        if (
                            int(d_limit) != matrix.row_limit
                            or int(h_limit) != matrix.col_limit
                        ):
                            alert_msgbox(
                                "Sistema No Actualizado",
                                f"Los limites deben ser iguales a los ya ingresados\nSistema de Drones: {system_name}",
                            )
                            error = True
                            continue
                        # temp = matrix.rows
                        t = matrix.verify_dup(dron)

                        if t:
                            temp = t.value
                            update_row = True

                    if matrix.rows.size > matrix.row_limit - 1 and not update_row:
                        alert_msgbox(
                            "Limite de Drones alcanzado",
                            f"Dron {dron} omitido\nSistema de drones: {system_name}",
                        )
                        continue

                    if not self.list_dron.verify_dup(dron):
                        error_msgbox(
                            "Error",
                            f"El dron {dron} no esta en la lista de drones\nSistema de Drones: {system_name} omitido",
                        )
                        error = True
                        continue
                    for Hight in content.findall("alturas"):
                        for h in Hight.findall("altura"):
                            value = h.text
                            if int(h.get("valor")) <= 0:
                                continue
                            if int(h.get("valor")) <= int(h_limit):
                                if value is None:
                                    value = " "

                                if not temp.verify_replace(int(h.get("valor")), value):
                                    # print(int(h.get("valor")), value, "¿¿¿")
                                    temp.insert_sorted(int(h.get("valor")), value)
                    if not update_row:
                        matrix.create_matrix(dron, temp)
                if not error and not update_all:
                    list_ori.insert_sorted(system_name, matrix)
                # print(temp.size, "--")
            # print()

    def load_list_mes(self, list_ori: LinkedList):
        for m_list in self.root.findall("listaMensajes"):
            for message in m_list.findall("Mensaje"):
                error = False
                message_name = message.get("nombre")
                system_name = message.findtext("sistemaDrones")
                list_ins = DoublyLinkedListSistem()
                validate = self.list_sistem.verify_dup(system_name)
                upadate = False
                max_c = None
                if not validate:
                    error_msgbox(
                        "Error",
                        f"El Systema {system_name} no está registrado",
                    )
                    continue
                max_c = validate.value.col_limit

                temp_list = list_ori.verify_dup(message_name)

                if temp_list:
                    if temp_list.name_system != system_name:
                        error_msgbox(
                            "Error",
                            f"Sistema de drones en {message_name} \nSon diferentes, se omite el mensjae",
                        )
                    list_ins = temp_list.value
                    temp_list.processed = False
                    upadate = True
                    # continue

                for instructions in message.findall("instrucciones"):
                    for i in instructions.findall("instruccion"):
                        if error:
                            continue
                        value = int(i.text)
                        dup = list_ins.search_from_end(i.get("dron"))
                        # dup = list_ins.search_from_end(i.get("dron"

                        if not self.list_dron.verify_dup(i.get("dron")):
                            alert_msgbox(
                                "Error",
                                f"El dron {i.get('dron')} no esta en la lista de drones",
                            )
                            # error = True
                            continue
                        rows = self.list_sistem.verfy_dron_m(system_name, i.get("dron"))
                        if not rows:
                            alert_msgbox(
                                "Error",
                                f"El dron {i.get('dron')} no está\nen el sistema de drones {system_name}",
                            )
                            # error = True
                            continue

                        if int(i.text) > max_c:
                            alert_msgbox(
                                "Error",
                                f"La altura {i.text} esta fuera de rango Limite: {max_c}\nSistema de dron: {system_name}",
                            )
                            continue

                        times = rows.value
                        if not times.verfy_dron_hight(int(i.text)):
                            alert_msgbox(
                                "Error",
                                f"El dron {i.get('dron')} no tiene una altura {i.text}\nLinea Omitida",
                            )
                            continue

                        if dup:
                            value -= dup.h_inst
                        list_ins.insert(i.get("dron"), value, int(i.text))
                if not error and not upadate:
                    if list_ins.size != 0:
                        list_ori.insert_sorted_msg(
                            message_name,
                            list_ins,
                            system_name,
                            validate.value.row_limit,
                        )
                    else:
                        error_msgbox(
                            "Advertencia", f"{message_name} no tiene instrucciones"
                        )
