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
                if int(h_limit) > 100:
                    alert_msgbox(
                        "Advertencia",
                        "El limite de alturas permitido es 100\nSe cambia las alturas a 100",
                    )
                if int(d_limit) > 200:
                    alert_msgbox(
                        "Advertencia",
                        "El limite de drones permitido es 200\nSe cambia el No. Drones a 200",
                    )
                matrix = MainSistem(int(d_limit), int(h_limit))
                error = False
                update = False
                for content in sistem_l.findall("contenido"):
                    if error:
                        continue

                    dron = content.findtext("dron")
                    temp = LinkedList()
                    temp_list = self.list_sistem.verify_dup(system_name)
                    if temp_list:
                        matrix = temp_list.value
                        print(matrix.rows.size, matrix.row_limit, "---")
                        if matrix.rows.size > matrix.row_limit - 1:
                            error = True
                            print(matrix.rows.size, matrix.row_limit)
                            break
                        if (
                            int(d_limit) < matrix.row_limit
                            or int(h_limit) < matrix.col_limit
                        ):
                            error_msgbox(
                                "Error",
                                "No se puede tener un limite inferior al ya ingresado",
                            )

                        # temp = matrix.rows
                        t = matrix.verify_dup(dron)
                        if t:
                            temp = t.value
                            update = True
                    if not self.list_dron.verify_dup(dron):
                        error_msgbox(
                            "Error",
                            f"El dron {dron} no esta en la lista de drones\nNo se agregará el sistema",
                        )
                        error = True
                        continue
                    for Hight in content.findall("alturas"):
                        for h in Hight.findall("altura"):
                            value = h.text

                            if int(h.get("valor")) <= int(h_limit):
                                if value is None:
                                    value = " "
                                if temp.verify_replace(int(h.get("valor")), value):
                                    update = True
                                else:
                                    temp.insert_sorted(int(h.get("valor")), value)
                                    update = False
                                # print(h.get("valor"), value)
                            else:
                                error_msgbox(
                                    "Error",
                                    f"Altura: {h.get('valor')}\nMayor al limite del sistema: {system_name}",
                                )
                    if not update:
                        matrix.create_matrix(dron, temp)
                if not error and not update:
                    list_ori.insert_sorted(system_name, matrix)
                # print(matrix.rows, system_name)
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
                        # dup = list_ins.search_from_end(i.get("dron"))

                        if not self.list_dron.verify_dup(i.get("dron")):
                            error_msgbox(
                                "Error",
                                f"El dron {i.get('dron')} no esta en la lista de drones",
                            )
                            # error = True
                            continue

                        if not self.list_sistem.verfy_dron_m(
                            system_name, i.get("dron")
                        ):
                            error_msgbox(
                                "Error",
                                f"El dron {i.get('dron')} no esta en el sistema de drones {system_name}",
                            )
                            # error = True
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
                if not error and not upadate:
                    list_ori.insert_sorted_msg(
                        message_name, list_ins, system_name, validate.value.row_limit
                    )
