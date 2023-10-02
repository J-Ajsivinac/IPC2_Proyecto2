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
            self.size += 1
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
            self.size += 1
        else:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node
            self.size += 1

    def search_binary_dup(self, name):
        if not self.first:
            return None

        left = self.first
        right = self.end
        # print(f"double:{left.i_d}--{right.i_d}")
        while left is not None and right is not None:
            if left.i_d > right.i_d:
                if left.i_d == name:
                    return left
                break
            if left.i_d == right.i_d:
                if left.i_d == name:
                    return left
                return None
            if left.i_d == name:
                return left
            if right.i_d == name:
                return right

            left = left.next_node
            right = right.last_node

        if left and left.i_d == name:
            return left
        if right and right.i_d == name:
            return right
        return None

    def verify_replace(self, i_d, value, h):
        current = self.first
        while current:
            if current.i_d == i_d:
                current.value = value
                current.h_inst = h
                return True
            current = current.next_node
        return False

    def search_binary_next(self, name):
        if not self.first:
            return None

        left = self.first
        right = self.end
        # print(f"double:{left.i_d}--{right.i_d}")
        while True:
            if left is not None:
                if left.i_d == name:
                    return left
                left = left.next
            if right is not None:
                if right.i_d == name:
                    return right
                right = right.prev
            if left is None and right is None:
                break
        return None

    def search_from_end(self, value):
        last = self.end
        while last and last.i_d != value:
            last = last.last_node

        # while last and last.i_d != value:
        #     last = last.last_node

        if last:
            return last
        return None

    def delete_f(self):
        if self.first:
            # print(self.first.i_d, self.first.value, self.first.h_inst)
            if self.first.next_node:
                temp = self.first
                self.first = temp.next_node
                temp.next_node.last_node = None
                temp.next_node = None
                if not self.first.next_node:
                    self.end = self.first
            else:
                self.first = None
                self.end = None

            self.size -= 1
        # print("")

    def print_d(self):
        current = self.first
        while current:
            print(current.i_d, current.value, current.h_inst)
            current = current.next_node

    def crete_temp(self):
        list_temp = DoublyLinkedListSistem()
        current = self.first
        while current:
            # print(current.i_d, current.value, current.h_inst)
            comp = current.i_d
            validate = list_temp.search_binary_next(comp)
            # print(validate, current.i_d, current.value, current.h_inst, "---")
            if validate is None:
                current.next = None
                current.prev = None
                list_temp.insert_node(current)
            current = current.next_node
        # print("")
        return list_temp

    def optimize(self, matrix):
        list_temp = self.crete_temp()
        current = list_temp.first
        count = 0
        # print("...")
        # list_temp.print_d()
        # print("...")
        while current:
            # if current:
            #     print("--", current.i_d, current.value, current.h_inst)
            h = current.value
            if h < 0:
                h = h * -1

            for _ in range(h + 1):
                matrix.instructions(list_temp, count)
                count += 1

            self.delete_f()
            # list_temp.delete_f()
            list_temp = None
            list_temp = self.crete_temp()

            current = list_temp.first

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
                    for _ in range(current_instructions.h_inst - 1):
                        current_list = current_list.next_node
                    if current_list is not None:
                        message += current_list.value
                        break
                current = current.next_node
            current = matrix.rows.first
            current_instructions = current_instructions.next_node
        # print(message)
        return message

    def empty_list(self):
        self.first = None
        self.end = None
        self.size = 0
