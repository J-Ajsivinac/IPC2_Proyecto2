from Tdas.doublyLinkedList import DoublyLinkedListSistem
from Tdas.linkedListD import LinkedListDrone


class MainSistem:
    def __init__(self, rows, columns):
        self.rows = LinkedListDrone()
        self.row_limit = 100 if rows > 100 else rows
        self.col_limit = 200 if columns > 200 else columns

    # name, id
    def create_matrix(self, hight, row):
        if self.col_limit <= int(hight):
            self.rows.insert_sorted(hight, row)

    def display_matrix(self, name_system):
        current = self.rows.first
        print(name_system)
        while current:
            c_1 = current.i_d.first
            while c_1:
                print(str(c_1.letter), end="\t")
                c_1 = c_1.next_node
            print(" ")
            current = current.next_node
        print(" ")
