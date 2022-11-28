from abc import ABC, abstractmethod

from typing import List


class Graph(ABC):
    def __init__(self, v: int):
        self.vertices = v

    @abstractmethod
    def get_cost(self, i: int, j: int):
        pass


class MatrixGraph(Graph):
    def __init__(self, v: int, matrix: List[List[int]]):
        super().__init__(v)
        self.adjMatrix = matrix

    def get_cost(self, i: int, j: int):
        return self.adjMatrix[i][j]


class tupGraph(Graph):
    def __init__(self, v: int, l: List[tuple]):
        super().__init__(v)
        self.edges = l

    def get_cost(self, i: int, j: int):
        w = float('inf')
        for edge in self.edges:
            if (edge[0] == i and edge[1] == j) or (edge[0] == j and edge[1] == i):
                w = edge[2]
                break
        return w

class Mst(ABC):
    def __init__(self):
        self.a = 0

    @abstractmethod
    def add_branch_to_mst(self, edge: tuple, weight: int):
        pass

    @abstractmethod
    def result(self):
        return None


class MstKeepingSum(Mst):
    def __init__(self):
        super().__init__()
        self.sum = 0

    def add_branch_to_mst(self, edge: tuple, weight: int):
        self.sum += weight

    def result(self):
        return self.sum


class MstKeepingBranches(MstKeepingSum):
    def __init__(self):
        super().__init__()
        self.branches = []

    def add_branch_to_mst(self, edge: tuple, weight: int):
        super().add_branch_to_mst(edge, weight)
        self.branches.append(edge)

    def result(self):
        return self.branches


class MstFullDetails(Mst):
    def __init__(self):
        super().__init__()
        self.full = {'branches': [], 'sum cost': 0}

    def add_branch_to_mst(self, edge: tuple, weight: int):
        super().add_branch_to_mst(edge, weight)
        self.full['branches'].append(edge)
        self.full['sum cost'] += weight

    def result(self):
        return self.full


