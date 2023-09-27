import graphviz
from Tdas.linkedListD import LinkedListDrone


class Graph:
    def __init__(self, name):
        self.name = name
        self.dot = graphviz.Digraph(f"{name}", filename=f"{name}.gv", format="svg")

    def create_sistem(self, list_sys: LinkedListDrone):
        current = list_sys.first
        i = 0
        while current:
            # print(current.i_d, current.value)
            with self.dot.subgraph(name=f"cluster_{i}") as cl:
                # cl.node("header", label=f"{current.i_d}")
                table_html = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="lightgrey">'

                # current_value = current.value
                current_matrix = current.value.rows.first
                rows = current_matrix.value.first
                times = current_matrix.value.size
                for m in range(times + 1):
                    temp = current.value.rows.first
                    table_html += "<TR>"
                    for x in range(current.value.row_limit + 1):
                        if temp is None:
                            break
                        columns = temp.value.first
                        if m == 0:
                            if x == 0:
                                table_html += "<TD>Altura (m)</TD>"
                            else:
                                table_html += f"<TD>{temp.i_d}</TD>"
                                temp = temp.next_node
                        else:
                            if x == 0:
                                table_html += f"<TD>{m}</TD>"
                            else:
                                for _ in range(m - 1):
                                    columns = columns.next_node
                                table_html += f"<TD>{columns.value}</TD>"
                                temp = temp.next_node
                    if m != 1:
                        rows = rows.next_node
                    # current_matrix = current.value.rows.first
                    table_html += "</TR>"

                # current = current.next_node
                table_html += "</TABLE>>"
                # print(table_html)
                # print()
                cl.node(f"table_{i}", label=table_html)
                i += 1
                current = current.next_node

        self.dot.render(outfile=f"{self.name}.svg", format="svg", view=True)
