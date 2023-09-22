from Tdas.nodeS import NodeSistem


class DoublyLinkedListSistem:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def insert_sorter(self, name, letter):
        new_data = NodeSistem(name, letter)

        if not self.first:
            self.first = new_data
            self.end = new_data
        else:
            current = self.first
            while current and current.name < name:
                current = current.next_node

            # insertar datos al final
            if not current:
                last_n = self.first
                while last_n.next_node:
                    last_n = last_n.next_node
                last_n.next_node = new_data
                new_data.last_node = last_n
                self.end = new_data
            # insertar datos al inicio
            elif not current.last_node:
                new_data.next_node = self.first
                self.first.last_node = new_data
                self.first = new_data
                if not new_data.next_node:
                    self.end = new_data
            # Insertar datos en medio
            else:
                new_data.last_node = current.last_node
                new_data.next_node = current
                current.last_node.next_node = new_data
                current.last_node = new_data

        self.size += 1

    def is_name_repeated_binary_search(self, name):
        if not self.first:
            return None

        left = self.first
        right = self.end

        while left is not None and right is not None and left != right:
            mid = left
            while mid.next_node != right:
                mid = mid.next_node

            if left.name == name:
                return left.letter
            if right.name == name:
                return right.name
            if mid.name == name:
                return mid.letter

            if name < mid.name:
                right = mid
            else:
                left = mid.next_node

        return None
