from Tdas.nodeD import NodeDrone
from Tdas.nodeM import NodeMessage
from components.customMessage import *
from Tdas.mainS import MainSistem
import copy


class LinkedList:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    # Nombre, matriz
    def insert(self, i_d, value=None):
        new_node = NodeDrone(i_d, value)
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

    def insert_sorted(self, i_d, value=None):
        if self.verify_dup(i_d):
            # error_msgbox("Error", f"El nombre {i_d} ya está registrado --")
            return

        if not i_d:
            i_d = self.size + 1
        new_data = NodeDrone(i_d, value)
        if self.is_empty():
            self.first = new_data
            self.end = new_data
            new_data.next_node = None
        elif self.first.i_d >= i_d:
            new_data.next_node = self.first
            self.first = new_data

        else:
            current = self.first
            while current.next_node and current.next_node.i_d < i_d:
                current = current.next_node
            new_data.next_node = current.next_node
            current.next_node = new_data

            # Actualizar el nodo final si el nuevo nodo se inserta al final
            if not current.next_node:
                self.end = new_data
        self.size += 1

    def insert_sorted_msg(self, i_d, value, name_system, max_c):
        new_data = NodeMessage(i_d, value, name_system, max_c)
        if self.is_empty():
            self.first = new_data
            self.end = new_data
            new_data.next_node = None
        elif self.first.i_d > i_d:
            new_data.next_node = self.first
            self.first = new_data
        else:
            current = self.first
            while current.next_node and current.next_node.i_d < i_d:
                current = current.next_node
            new_data.next_node = current.next_node
            current.next_node = new_data

            # Actualizar el nodo final si el nuevo nodo se inserta al final
            if current == self.end:
                self.end = new_data

        self.size += 1

    def verify_dup(self, name):
        current = self.first
        prev = None

        if self.size == 0:
            return None

        while current and current.i_d != name:
            prev = current
            current = current.next_node

        if not current:
            return None
        if not prev:
            return current

        return current

    def verify_replace(self, name, value):
        current = self.first
        prev = None

        if self.size == 0:
            return False

        while current and current.i_d != name:
            prev = current
            current = current.next_node
        temp = NodeDrone(name, value)
        if not current:
            return False
        if prev is None:
            self.first = temp
            temp.next_node = current.next_node
            current.next_node = None
            return True

        prev.next_node = temp
        temp.next_node = current.next_node
        current.next_node = None
        return True

    def verify_replace_msg(self, name, value, name_system, max_c):
        current = self.first
        prev = None

        if self.size == 0:
            return False

        while current and current.i_d != name:
            prev = current
            current = current.next_node
        temp = NodeMessage(name, value, name_system, max_c)
        if not current:
            return False
        if prev is None:
            self.first = temp
            temp.next_node = current.next_node
            current.next_node = None
            return True

        if current is self.end:
            self.end = temp

        prev.next_node = temp
        temp.next_node = current.next_node
        current.next_node = None
        return True

    def s_search_b_hight(self, name):
        if not self.first:
            return None

        left = self.first
        right = self.end
        # print(name, left.i_d, right.i_d)
        while left is not None and right is not None and left.i_d != right.i_d:
            mid = left
            while mid.next_node.i_d != right.i_d:
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
        if left and left.i_d == name:
            return left
        if right and right.i_d == name:
            return right
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

    def call_optimize(self, list_sistem, list_proc):
        current_o = self.first
        current = copy.deepcopy(self.first)
        temp = None

        while current:
            if current.processed or current is None:
                current = current.next_node
                curren_o = current_o.next_node
                continue

            matrix = MainSistem(columns=current.max_columns)
            validate = list_sistem.verify_dup(current.name_system)
            current_dron = validate.value.rows.first
            # print(current.max_columns)
            for _ in range(matrix.col_limit):
                if current_dron:
                    temp = LinkedList()
                    matrix.create_matrix_instr(current_dron.i_d, temp)
                    current_dron = current_dron.next_node

            # print(validate.value)
            message = current.value.decode(validate.value)
            _ = current.value.optimize(matrix)
            current.processed = True
            current_o.processed = True
            if not list_proc.verify_replace_msg(
                current.i_d, matrix, message, current.name_system
            ):
                list_proc.insert_sorted_msg(
                    current.i_d, matrix, message, current.name_system
                )
            current = copy.deepcopy(current.next_node)
            current_o = current_o.next_node

    def empty_list(self):
        self.first = None
        self.end = None
        self.size = 0

    def update_value(self, i_d, new_value):
        current = self.first
        while current:
            if current.i_d == i_d:
                if current.value != new_value:
                    current.value = new_value
                break
            current = current.next_node

    def verfy_dron_m(self, name_s, dron):
        current = self.first
        while current:
            if current.i_d == name_s:
                rows = current.value.rows
                result = rows.search_binary_dup(dron)
                return result
            current = current.next_node
        return None
