from Tdas.nodeD import NodeDrone


class NodeSistem(NodeDrone):
    def __init__(self, i_d, value):
        super().__init__(i_d, None, None)
        self.value = value
        self.last_node = None
        self.next_node = None
