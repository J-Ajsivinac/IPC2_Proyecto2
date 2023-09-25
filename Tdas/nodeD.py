# Clase para los drones
class NodeDrone:
    def __init__(self, i_d, value, processed=False):
        self.i_d = i_d
        self.value = value
        self.processed = processed
        self.next_node = None
