# Clase para los drones
class NodeDrone:
    def __init__(self, i_d, value, name_system):
        self.i_d = i_d
        self.value = value
        self.name_system = name_system
        self.next_node = None
