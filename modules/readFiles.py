import xml.etree.ElementTree as ET
from Tdas.linkedListD import LinkedListDrone
from Tdas.doublyLinkedList import DoublyLinkedListSistem
from Tdas.mainS import MainSistem


class Read:
    def read_file(self, route):
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()

    def load_data(self, list_dron, list_sistem, list_messages):
        self.load_drones(list_dron)
        self.load_list_drone(list_sistem)
        self.load_list_mes(list_messages)
        # list_dron.print_drone()
        # list_sistem.print_temp()
        list_messages.print_temp1()

    def load_drones(self, list_ori: LinkedListDrone):
        for list_d in self.root.findall("listaDrones"):
            for dron in list_d.findall("dron"):
                list_ori.insert_sorted(dron.text)

    def load_list_drone(self, list_ori: LinkedListDrone):
        for list_ in self.root.findall("listaSistemasDrones"):
            for sistem_l in list_.findall("sistemaDrones"):
                # recuperar datos del XML
                system_name = sistem_l.get("nombre")
                h_limit = sistem_l.findtext("alturaMaxima")
                d_limit = sistem_l.findtext("cantidadDrones")
                matrix = MainSistem(int(d_limit), int(h_limit))

                for content in sistem_l.findall("contenido"):
                    dron = content.findtext("dron")
                    temp = LinkedListDrone()
                    for Hight in content.findall("alturas"):
                        for h in Hight.findall("altura"):
                            if int(h.get("valor")) <= int(h_limit):
                                temp.insert_sorted(h.get("valor"), h.text)
                    matrix.create_matrix(dron, temp)
                list_ori.insert_sorted(system_name, matrix)
                # print(matrix.rows, system_name)

    def load_list_mes(self, list_ori: LinkedListDrone):
        for m_list in self.root.findall("listaMensajes"):
            for message in m_list.findall("Mensaje"):
                message_name = message.get("nombre")
                system_name = message.findtext("sistemaDrones")
                # matrix_temp = MainSistem()
                list_ins = DoublyLinkedListSistem()
                for instructions in message.findall("instrucciones"):
                    for i in instructions.findall("instruccion"):
                        value = int(i.text)
                        dup = list_ins.search_binary_dup(i.get("dron"))
                        if dup:
                            value -= dup
                        list_ins.insert(i.get("dron"), value)
                list_ori.insert_sorted(message_name, list_ins, system_name)
