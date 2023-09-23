from Tdas.doublyLinkedList import DoublyLinkedListSistem
from Tdas.linkedListD import LinkedListDrone


class MainSistem:
    def __init__(self, rows=0, columns=0):
        self.rows = DoublyLinkedListSistem()
        self.row_limit = 100 if rows > 100 else rows
        self.col_limit = 200 if columns > 200 else columns

    # name, id
    def create_matrix(self, hight, row):
        self.rows.insert_sorter(hight, row)

    def verify_dup_row(self, value):
        pass

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
