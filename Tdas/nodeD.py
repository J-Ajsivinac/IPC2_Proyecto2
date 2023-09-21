# Clase para los drones
class NodeDrone:
    def __init__(self, name, i_d, letter=None):
        self.i_d = i_d
        self.name = name
        self.letter = letter
        self.next_node = None
