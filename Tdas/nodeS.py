from Tdas.nodeD import NodeDrone


class NodeSistem(NodeDrone):
    def __init__(self, name, letter):
        super().__init__(name, None)
        self.letter = letter
        self.last_node = None
        self.next_node = None
