from Tdas.nodeS import NodeSistem
from components.customMessage import *


class DoublyLinkedListSistem:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def insert(self, i_d, letter, h_inst=None):
        new_data = NodeSistem(i_d, letter, h_inst)
        if not self.first:
            self.first = new_data
            self.end = new_data
        else:
            new_data.last_node = self.end
            self.end.next_node = new_data
            self.end = new_data
        self.size += 1

    def insert_sorter(self, i_d, letter, h_inst=None):
        new_data = NodeSistem(i_d, letter, h_inst)
        if self.search_binary_dup(i_d):
            error_msgbox("Error", f"El nombre {i_d} ya está registrado")
            return
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

    def insert_node(self, new_node):
        if not self.first:
            self.first = new_node
            self.end = new_node
        else:
            new_node.prev_node = self.end
            self.end.next_node = new_node
            self.end = new_node

    def search_binary_dup(self, name):
        if not self.first:
            return None

        left = self.first
        right = self.end
        # print(f"double:{left.i_d}--{right.i_d}")
        while left is not None and right is not None and left != right:
            mid = left
            while mid.next_node != right:
                mid = mid.next_node

            if left.i_d == name:
                return left
            if right.i_d == name:
                return right
            if mid.i_d == name:
                return mid

            if name < mid.i_d:
                right = mid.last_node
            else:
                left = mid.next_node
        if left and left.i_d == name:
            return left
        if right and right.i_d == name:
            return right
        return None

    def search_from_end(self, value):
        last = self.end
        while last and last.i_d != value:
            last = last.last_node

        while last and last.i_d != value:
            last = last.last_node

        if last:
            return last
        return None

    def delete_f(self):
        if self.first:
            # current = self.first
            self.first = self.first.next_node
            if self.first:
                self.first.last_node = None
            else:
                self.end = None
            self.size -= 1

    def print_d(self):
        current = self.first
        while current:
            print(current.i_d, current.value, current.h_inst)
            current = current.next_node

    def crete_temp(self):
        list_temp = DoublyLinkedListSistem()
        current = self.first
        while current:
            if list_temp.search_binary_dup(current.i_d):
                current = current.next_node
                continue
            # new_node = NodeSistem(current.i_d, current.value, current.h_inst)
            list_temp.insert_node(current)
            # print(current.i_d, current.value, current.h_inst)
            current = current.next_node
        return list_temp

    def optimize(self, matrix):
        list_temp = self.crete_temp()
        current = list_temp.first
        count = 0
        while current:
            h = current.value
            if h < 0:
                h = h * -1

            for _ in range(h + 1):
                matrix.instructions(list_temp, count)
                count += 1

            self.delete_f()

            list_temp = self.crete_temp()
            current = list_temp.first

            # print("--")
            # current = current.next_node
        return count

    def decode(self, matrix):
        current_instructions = self.first
        current = matrix.rows.first
        message = ""
        while current_instructions:
            while current:
                if current.i_d == current_instructions.i_d:
                    # print(current.value, "--")
                    current_list = current.value.first
                    for _ in range(current_instructions.value - 1):
                        current_list = current_list.next_node
                    if current_list is not None:
                        message += current_list.value
                        break
                current = current.next_node
            current = matrix.rows.first
            current_instructions = current_instructions.next_node

        return message
