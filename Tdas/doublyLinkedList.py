from Tdas.nodeS import NodeSistem


class DoublyLinkedListSistem:
    def __init__(self):
        self.first = None

    def insert_sorter(self, name, letter):
        new_data = NodeSistem(name, letter)

        if not self.first:
            self.first = new_data
        else:
            current = self.first
            while current and current.name < name:
                current = current.next_node

            # insertar datos al final
            if not current:
                last_n = self.first
                while last_n.next_node:
                    last_n = last_n.next_node
                last_n.next_node = new_data
                new_data.last_node = last_n
            # insertar datos al inicio
            elif not current.last_node:
                new_data.next_node = self.first
                self.first.last_node = new_data
                self.first = new_data
            # Insertar datos en medio
            else:
                new_data.last_node = current.last_node
                new_data.next_node = current
                current.last_node.next_node = new_data
                current.last_node = new_data
