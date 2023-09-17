from Tdas.nodeD import NodeDrone


class LinkedListDrone:
    def __init__(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def insert_sorted(self, data):
        new_data = NodeDrone(data)
        if self.is_empty():
            self.first = new_data
            new_data.next_node = None
        elif self.first.name > data:
            new_data.next_node = self.first
            self.first = new_data
        else:
            current = self.first
            while current.next_node.name > data and current.next_node:
                current = current.next_node
            new_data.next_node = current.next_node
            current.next_node = new_data

    def verify_dup(self, name):
        current = self.first
        prev = None

        if self.size == 0:
            return False

        while current and current.name != name:
            prev = current
            current = current.next_node

        if not current:
            return False
        if not prev:
            return True

        return True

    def print_drone(self):
        current = self.first
        while current:
            print(current.name)
            current = current.next_node
