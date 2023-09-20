import xml.etree.ElementTree as ET
from Tdas.linkedListD import LinkedListDrone
from Tdas.doublyLinkedList import DoublyLinkedListSistem
from Tdas.mainS import MainSistem


class Read:
    def read_file(self, route):
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()

    def load_data(self, list_dron, list_sistem):
        self.load_drones(list_dron)
        self.load_list_drone(list_sistem)
        # list_dron.print_drone()
        list_sistem.print_temp()

    def load_drones(self, list_ori: LinkedListDrone):
        for list_d in self.root.findall("listaDrones"):
            for dron in list_d.findall("dron"):
                list_ori.insert_sorted(dron.text)

    def load_list_drone(self, list_ori: LinkedListDrone):
        for list_ in self.root.findall("listaSistemasDrones"):
            for sistem_l in list_.findall("sistemaDrones"):
                # recuperar limites
                temp = DoublyLinkedListSistem()
                system_name = sistem_l.get("nombre")
                h_limit = sistem_l.findtext("alturaMaxima")
                d_limit = sistem_l.findtext("cantidadDrones")
                matrix = MainSistem(int(d_limit), int(h_limit))
                # print(h_limit, d_limit)
                for content in sistem_l.findall("contenido"):
                    dron = content.findtext("dron")
                    for Hight in content.findall("alturas"):
                        for h in Hight.findall("altura"):
                            if int(h.get("valor")) <= int(h_limit):
                                temp.insert_sorter(h.get("valor"), h.text)
                                # print(h.get("valor"), h.text, dron)
                        matrix.create_matrix(dron, temp)
                list_ori.insert(matrix, system_name)

    def load_list_mes(self):
        for m_list in self.root.findall("listaMensajes"):
            for message in self.root.findall("Mensaje"):
                # sistema
                for inst in self.root.findall("instrucciones"):
                    pass
