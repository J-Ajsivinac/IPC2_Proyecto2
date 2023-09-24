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
                return left
            if right.i_d == name:
                return right
            if mid.i_d == name:
                return mid

            if name < mid.i_d:
                right = mid
            else:
                left = mid.next_node

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
            list_temp.insert(current.i_d, current.value, current.h_inst)
            current = current.next_node
        return list_temp

    def optimize(self):
        list_temp = self.crete_temp()
        current = list_temp.first
