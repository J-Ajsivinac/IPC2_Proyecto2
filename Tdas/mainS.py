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

    def instructions(self, list_temp, number):
        left = self.rows.first
        right = self.rows.end
        p_drone = list_temp.first.i_d
        # print(current_dron.i_d)
        while left and right:
            if left.i_d > right.i_d:
                break

            if left.i_d == right.i_d:
                # print(f"--{left.i_d},{right.value}")
                search = list_temp.search_binary_dup(right.i_d)
                # print("value", search.value)
                if not search:
                    left.value.insert(number, "Esperar")
                elif search.value > 0:
                    # print("Subir", right.i_d)
                    left.value.insert(number, "Subir")
                    search.value -= 1
                elif search.value < 0:
                    # print("Bajar", right.i_d)
                    left.value.insert(number, "Bajar")
                    search.value += 1
                elif search.value == 0:
                    if search.i_d == p_drone:
                        # print("Encender", right.i_d)
                        left.value.insert(number, "Encender")
                        # search.value -= 1
                    else:
                        # print("Esperar", right.i_d)
                        left.value.insert(number, "Esperar")
                break

            if left:
                search = list_temp.search_binary_dup(left.i_d)

                if not search:
                    left.value.insert(number, "Esperar")

                elif search.value > 0:
                    # print("Subir", left.i_d)
                    left.value.insert(number, "Subir")
                    search.value -= 1
                elif search.value < 0:
                    # print("Bajar", left.i_d)
                    left.value.insert(number, "Bajar")
                    search.value += 1
                elif search.value == 0:
                    if search.i_d == p_drone:
                        # print("Encender", left.i_d)
                        left.value.insert(number, "Encender")
                        # search.value -= 1
                    else:
                        # print("Esperar", left.i_d)
                        left.value.insert(number, "Esperar")

            if right:
                search = list_temp.search_binary_dup(right.i_d)
                if not search:
                    right.value.insert(number, "Esperar")
                elif search.value > 0:
                    # print("Subir", right.i_d)
                    right.value.insert(number, "Subir")
                    search.value -= 1
                elif search.value < 0:
                    # print("Bajar", right.i_d)
                    right.value.insert(number, "Bajar")
                    search.value += 1
                elif search.value == 0:
                    if search.i_d == p_drone:
                        # print("Encender", right.i_d)
                        right.value.insert(number, "Encender")
                        search.value -= 1
                    else:
                        # print("Esperar", right.i_d)
                        right.value.insert(number, "Esperar")

            left = left.next_node
            right = right.last_node
