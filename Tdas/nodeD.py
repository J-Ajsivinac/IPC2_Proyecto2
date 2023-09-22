# Clase para los drones
class NodeDrone:
    def __init__(self, name, i_d, temp=None):
        self.i_d = i_d
        self.name = name
        self.temp = temp
        self.next_node = None
