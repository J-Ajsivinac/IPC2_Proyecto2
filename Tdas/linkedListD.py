from Tdas.nodeD import NodeDrone


class LinkedListDrone:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    # Nombre, matriz
    def insert(self, data, i_d=None, temp=None):
        new_node = NodeDrone(data, i_d, temp)
        if self.is_empty():
            self.first = new_node
            self.end = new_node
            self.size += 1
            return
        current = self.first
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        self.end = current.next_node
        self.size += 1

    def insert_sorted(self, data, i_d=None, temp=None):
        if not i_d:
            i_d = self.size + 1
        new_data = NodeDrone(data, i_d, temp)
        if self.is_empty():
            self.first = new_data
            self.end = new_data
            new_data.next_node = None
        elif self.first.name > data:
            temp = self.first
            new_data.next_node = self.first
            self.first = new_data
            if not new_data.next_node:
                self.end = temp
        else:
            current = self.first
            while current.next_node and current.next_node.name < data:
                current = current.next_node
            new_data.next_node = current.next_node
            current.next_node = new_data
        self.size += 1

    def verify_dup(self, name):
        current = self.first
        prev = None

        if self.size == 0:
            return None

        while current and current.name != name:
            prev = current
            current = current.next_node

        if not current:
            return None
        if not prev:
            return current

        return current

    def print_drone(self):
        current = self.first
        while current:
            print(current.name)
            current = current.next_node

    def print_temp(self):
        current = self.first
        while current:
            current.i_d.display_matrix(current.name)
            current = current.next_node

    def print_temp1(self):
        current = self.first
        while current:
            current.i_d.display_instrucciones(current.name)
            current = current.next_node
