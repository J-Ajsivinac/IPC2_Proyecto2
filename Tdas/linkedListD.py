from Tdas.nodeD import NodeDrone
from components.customMessage import *
from Tdas.mainS import MainSistem


class LinkedListDrone:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    # Nombre, matriz
    def insert(self, i_d, value=None, temp=None):
        new_node = NodeDrone(i_d, value, temp)
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

    def insert_sorted(self, i_d, value=None, temp=None):
        if self.verify_dup(i_d):
            error_msgbox("Error", f"El nombre {i_d} ya está registrado")
            return

        if not i_d:
            i_d = self.size + 1
        new_data = NodeDrone(i_d, value, temp)
        if self.is_empty():
            self.first = new_data
            self.end = new_data
            new_data.next_node = None
        elif self.first.i_d > i_d:
            temp = self.first
            new_data.next_node = self.first
            self.first = new_data
            if not new_data.next_node:
                self.end = temp
        else:
            current = self.first
            while current.next_node and current.next_node.i_d < i_d:
                current = current.next_node
            new_data.next_node = current.next_node
            current.next_node = new_data
        self.size += 1

    def verify_dup(self, name):
        current = self.first
        prev = None

        if self.size == 0:
            return False

        while current and current.i_d != name:
            prev = current
            current = current.next_node

        if not current:
            return False
        if not prev:
            return current

        return current

    def s_search_b_hight(self, name):
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

    def print_drone(self):
        current = self.first
        while current:
            print(current.i_d)
            current = current.next_node

    def print_temp(self):
        current = self.first
        while current:
            current.value.display_matrix(current.i_d)
            current = current.next_node

    def print_temp1(self):
        current = self.first
        while current:
            print(current.i_d)
            current.value.print_d()
            current = current.next_node

    def call_optimize(self, list_instructions):
        current = self.first
        temp = None

        while current:
            print(current.value)
            # matrix = MainSistem()
            current.value.optimize()
            current = current.next_node
            # print(temp)
