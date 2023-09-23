from Tdas.nodeS import NodeSistem


class DoublyLinkedListSistem:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def insert(self, i_d, letter):
        new_data = NodeSistem(i_d, letter)
        if not self.first:
            self.first = new_data
            self.end = new_data
        else:
            new_data.last_node = self.end
            self.end.next_node = new_data
            self.end = new_data
        self.size += 1

    def insert_sorter(self, i_d, letter):
        new_data = NodeSistem(i_d, letter)
        if not self.first:
            self.first = new_data
            self.end = new_data
        else:
            current = self.first
            while current:
                if current.i_d > i_d:
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

            self.end.next_node = new_data
            new_data.last_node = self.end
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

            if left.i_d == name:
                return left.value
            if right.i_d == name:
                return right.value
            if mid.i_d == name:
                return mid.value

            if name < mid.i_d:
                right = mid
            else:
                left = mid.next_node

        return None

    def print_d(self):
        current = self.first
        while current:
            print(current.i_d, current.value)
            current = current.next_node
