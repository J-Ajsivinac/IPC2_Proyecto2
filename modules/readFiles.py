import xml.etree.ElementTree as ET
from Tdas.linkedListD import LinkedListDrone


class Read:
    def read_file(self, route):
        self.tree = ET.parse(route)
        self.root = self.tree.getroot()

    def load_data(self, list_drones):
        print("procesando")
        config = None
        self.load_drones(list_drones)
        list_drones.print_drone()

    def load_drones(self, list: LinkedListDrone):
        for list_d in self.root.findall("listaDrones"):
            for dron in list_d.findall("dron"):
                list.insert_sorted(dron.text)

    def load_list_drone(self):
        for list_ in self.root.findall("listaSistemasDrones"):
            for sistem_l in self.root.findall("sistemaDrones"):
                # recuperar limites
                for content in self.root.findall("contenido"):
                    pass  # dron, alturas
                    for h in self.root.findall("alturas"):
                        pass
            pass

    def load_list_mes(self):
        for m_list in self.root.findall("listaMensajes"):
            for message in self.root.findall("Mensaje"):
                # sistema
                for inst in self.root.findall("instrucciones"):
                    pass
