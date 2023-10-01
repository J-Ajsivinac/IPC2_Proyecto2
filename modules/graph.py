import graphviz
from Tdas.linkedListD import LinkedList


class Graph:
    def __init__(self, name):
        self.name = name
        self.dot = graphviz.Digraph(
            f"{name}",
            filename=f"{name}.gv",
            format="svg",
            node_attr={"fontname": "Verdana"},
        )

    def create_sistem(self, list_sys: LinkedList):
        current = list_sys.first
        i = 0
        while current:
            with self.dot.subgraph(name=f"cluster_{i}") as cl:
                cl.attr(
                    label=f"Sistema de Drones: {current.i_d}",
                    labelloc="t",
                    labeljust="c",
                    bgcolor="#eff6ff",
                    color="#bedbfe",
                    style="rounded",
                )
                table_html = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="white">'

                current_matrix = current.value.rows.first
                rows = current_matrix.value.first
                times = current.value.col_limit
                # print(times, current.value.col_limit)
                for m in range(times + 1):
                    temp = current.value.rows.first
                    # if rows:
                    table_html += "<TR>"
                    for x in range(current.value.row_limit + 1):
                        if temp is None:
                            table_html += '<TD BGCOLOR="#94979C"> </TD>'
                            continue
                        columns = temp.value
                        if m == 0:
                            if x == 0:
                                table_html += '<TD BGCOLOR="#2c2c2c"><FONT COLOR="white">Altura (m)</FONT></TD>'
                            else:
                                table_html += f'<TD BGCOLOR="#2c2c2c"><FONT COLOR="white">{temp.i_d}</FONT></TD>'
                                temp = temp.next_node
                        else:
                            if x == 0:
                                table_html += f"<TD>{m}</TD>"
                                continue
                            result = columns.verify_dup(m)
                            if result:
                                table_html += f"<TD>{result.value}</TD>"
                            else:
                                table_html += "<TD BGCOLOR='#94979C'> </TD>"
                            # print(x)
                            temp = temp.next_node
                    if m != 1:
                        if rows is None:
                            table_html += "</TR>"
                            continue
                        rows = rows.next_node
                    table_html += "</TR>"

                table_html += "</TABLE>>"
                cl.node(
                    f"table_{i}",
                    label=table_html,
                    shape="none",
                )
                i += 1
                current = current.next_node
        self.generate()

    def create_message(self, data):
        with self.dot.subgraph(name="cluster_1") as cl:
            cl.attr(
                bgcolor="#eff6ff",
                color="#bedbfe",
                style="rounded",
            )
            table_html = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="white">'

            current_matrix = data.value.rows.first
            rows = current_matrix.value.first
            times = current_matrix.value.size
            # print(times)
            # print(data.value.row_limit)
            for m in range(times + 1):
                temp = data.value.rows.first
                if temp is not None:
                    table_html += "<TR>"
                for x in range(data.value.col_limit + 1):
                    if temp is None:
                        continue
                    columns = temp.value.first
                    if m == 0:
                        if x == 0:
                            table_html += '<TD BGCOLOR="#2c2c2c"><FONT COLOR="white">Tiempo (s)</FONT></TD>'
                        else:
                            table_html += f'<TD BGCOLOR="#2c2c2c"><FONT COLOR="white">{temp.i_d}</FONT></TD>'
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
                table_html += "</TR>"

            table_html += "</TABLE>>"
            cl.node(
                "table",
                label=table_html,
                shape="none",
            )
        self.generate()

    def generate(self):
        name = f"resultados/{self.name}.svg".replace("\\", "/")
        try:
            self.dot.render(outfile=name, format="svg", view=True)
        except Exception as exce:
            print(exce)
