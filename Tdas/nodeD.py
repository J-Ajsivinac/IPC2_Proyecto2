# Clase para los drones
class NodeDrone:
    def __init__(self, name, i_d):
        self.i_d = i_d
        self.name = name
        self.next_node = None
