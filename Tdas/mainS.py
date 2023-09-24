from Tdas.doublyLinkedList import DoublyLinkedListSistem


class MainSistem:
    def __init__(self, rows=0, columns=0):
        self.rows = DoublyLinkedListSistem()
        self.row_limit = 100 if rows > 100 else rows
        self.col_limit = 200 if columns > 200 else columns

    # name, id
    def create_matrix(self, hight, row):
        self.rows.insert_sorter(hight, row)

    def create_matrix_instr(self, hight, row):
        self.rows.insert(hight, row)

    def display_matrix(self, name_system):
        current = self.rows.first
        print(name_system)
        while current:
            c_1 = current.value.first
            while c_1:
                print(str(c_1.value), end="\t")
                c_1 = c_1.next_node
            print(" ")
            current = current.next_node
        print(" ")

    def display_instrucciones(self, name_sys):
        print(name_sys)
        current = self.rows.first
        while current:
            temp = current.value.first
            while temp:
                print(temp.i_d)
                temp = temp.next_node
            current = current.next_node

    def instructions(self, list_temp):
        left = self.rows.first
        right = self.rows.end
        p_drone = list_temp.first.i_d
        current_dron = list_temp.first
        while left and right:
            print(f"left: {left.value}")
            # print(f"right: {right.i_d}")
            left = left.next_node
            right = right.last_node

            if left.i_d > right.i_d:
                break

            if left.i_d == right.i_d:
                print(f"igual:{left.i_d}")
                break
