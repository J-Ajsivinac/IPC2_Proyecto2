from Tdas.nodeD import NodeDrone


class NodeMessage(NodeDrone):
    def __init__(self, i_d, value, name_system, max_columns):
        super().__init__(i_d, value)
        self.name_system = name_system
        self.max_columns = max_columns
