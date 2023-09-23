from Tdas.nodeS import NodeSistem


class DoublyLinkedListSistem:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def insert(self, name, letter):
        new_data = NodeSistem(name, letter)
        if not self.first:
            self.first = new_data
            self.end = new_data
        else:
            new_data.last_node = self.end
            self.end.next_node = new_data
            self.end = new_data
        self.size += 1

    def insert_sorter(self, name, letter):
        new_data = NodeSistem(name, letter)
        if not self.first:
            self.first = new_data
            self.end = new_data
        else:
            current = self.first
            while current:
                if current.name > name:
                    if current.last_node:
                        current.last_node.next_node = new_data
                        new_data.last_node = current.last_node
                    else:
                        self.first = new_data
                    new_data.next_node = current
                    current.last_node = new_data
                    self.size += 1
                    return
                current = current.next_node
            self.first.next_node = new_data
            new_data.last_node = self.first
            self.end = new_data
            self.size += 1

    def search_binary_dup(self, name):
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

    def print_d(self):
        current = self.first
        while current:
            print(current.name, current.letter)
            current = current.next_node
