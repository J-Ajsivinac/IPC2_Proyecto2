from Tdas.doublyLinkedList import DoublyLinkedListSistem
from Tdas.linkedListD import LinkedListDrone


class MainSistem:
    def __init__(self, rows, columns):
        self.rows = DoublyLinkedListSistem()
        self.row_limit = 100 if rows > 100 else rows
        self.col_limit = 200 if columns > 200 else columns

    # name, id
    def create_matrix(self, hight, row):
        self.rows.insert_sorter(hight, row)

    def display_matrix(self, name_system):
        current = self.rows.first
        print(name_system)
        while current:
            c_1 = current.letter.first
            while c_1:
                print(str(c_1.i_d), end="\t")
                c_1 = c_1.next_node
            print(" ")
            current = current.next_node
        print(" ")
