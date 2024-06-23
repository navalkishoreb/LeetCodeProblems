from typing import List


class Edge:
    def __init__(self, vertex_a, vertex_b):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b

    def __eq__(self, other):
        if isinstance(other, Edge):
            return (
                self.vertex_a,
                self.vertex_b == other.vertex_a,
                other.vertex_b,
            )
        return False

    def __hash__(self):
        return hash((self.vertex_a, self.vertex_b))

    def __str__(self):
        return str((self.vertex_a, self.vertex_b))


def populate_edges(isConnected):
    edges = set()
    for row, row_data in enumerate(isConnected):
        for col, cell_value in enumerate(row_data):
            if cell_value == 1 and row != col:
                edges.add(Edge(vertex_a=row, vertex_b=col))
    return edges


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = populate_edges(isConnected)

        groups = list()
        for vertex in range(len(isConnected)):
            groups.append({vertex})

        for edge in edges:
            vertex_a, vertex_b = edge.vertex_a, edge.vertex_b
            connected_set = set()
            separate_set = list()
            for group in groups:
                if vertex_a in group or vertex_b in group:
                    connected_set.update(group)
                else:
                    separate_set.append(group)

            if connected_set:
                groups = list()
                groups.append(connected_set)
                groups.extend(separate_set)

        return len(groups)
