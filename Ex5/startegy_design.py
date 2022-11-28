from typing import Callable
from mst import *
import doctest


def getMST(algoritm: Callable, graph: list, mst: Mst = MstKeepingSum):
    """
    >>> INF = float('inf')
    >>> mat = [[INF, 2, 1, 6, 5],
    ...        [2, INF, 3, 8, 5],
    ...        [9, 3, INF, 4, 7],
    ...        [6, 8, 4, INF, 9],
    ...        [5, 5, 7, 9, INF]]
    >>> l = {'edges':[(0,1,2),(0,2,1),(0,3,6),(0,4,5),(1,2,3),
    ... (1,3,8),(1,4,5),(2,3,4),(2,4,7),(3,4,9)],'vertices':5}
    >>> getMST(Kruskal,mat,MstKeepingSum())
    12
    >>> getMST(Kruskal,l,MstKeepingSum())
    12
    >>> getMST(Prim,mat,MstKeepingSum())
    12
    >>> getMST(Prim,l,MstKeepingSum())
    12
    >>> k = {'edges':[(5,1,8),(0,2,4),(0,3,7),(0,6,9),(1,6,4),(1,2,7),
    ... (1,3,7),(1,4,8),(3,4,9),(6,4,7),(6,4,7),(2,4,9)],'vertices':6}
    >>> getMST(Prim,k,MstKeepingBranches())
    [(0, 2), (0, 3), (1, 2), (1, 4), (1, 5)]
    >>> getMST(Kruskal,mat,MstKeepingBranches())
    [(0, 2), (0, 1), (2, 3), (0, 4)]
    >>> getMST(Kruskal,mat,MstFullDetails())
    {'branches': [(0, 2), (0, 1), (2, 3), (0, 4)], 'sum cost': 12}
    >>> getMST(Prim,k,MstFullDetails())
    {'branches': [(0, 2), (0, 3), (1, 2), (1, 4), (1, 5)], 'sum cost': 34}
        """
    if isinstance(graph, dict):  # graph is a dict contain graph details.
        graph = tupGraph(graph['vertices'], graph['edges'])
    else:  # graph is a adjacency matrix
        graph = MatrixGraph(len(graph), graph)
    mst = algoritm(mst, graph)
    return mst.result()


def Kruskal(mst: Mst, graph: Graph) -> Mst:
    # init list to contain roots for each vertice
    parent = [i for i in range(graph.vertices)]

    def find(ind: int) -> int:
        """
        :param ind: index of vertice
        :return: root of this vertice
        """
        while parent[ind] != ind:
            ind = parent[ind]
        return ind

    def union(i, j) -> None:
        """
        union 2 trees: vertice i under vertice j
        """
        a = find(i)
        b = find(j)
        parent[a] = b

    edge_count = 0
    # get minimal edge for each vertice
    while edge_count < graph.vertices - 1:
        min = float('inf')
        a = b = -1
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                # If i and j are not in the same tree and edge(i,j) is minimal
                if find(i) != find(j) and graph.get_cost(i, j) < min:
                    min = graph.get_cost(i, j)
                    a = i
                    b = j
        # add to MST the edge(i,j)
        union(a, b)
        mst.add_branch_to_mst((a, b), min)
        edge_count += 1
    return mst


def Prim(mst: Mst, graph: Graph) -> Mst:
    # init list to know if each vertice inside MST (in same side of cut)
    inside = [True] + [False] * (graph.vertices - 1)

    def isValidEdge(u: int, v: int, inside: List[bool]) -> bool:
        """
        check if u,v are different, and not in same side of cut.
        """
        return not (u == v or inside[u] == inside[v])

    edge_count = 0
    # get minimum edge for each vertice
    while edge_count < graph.vertices - 1:

        min = float('inf')
        a = b = -1
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                # The function looks for an edge of minimum weight that crosses the
                # cut in the graph. Therefore, it checks each time whether the two
                # vertices are on both sides of the cut.
                if graph.get_cost(i, j) < min and isValidEdge(i, j, inside):
                    min = graph.get_cost(i, j)
                    a = i
                    b = j
        # if found edge that cross the cut, add it to MST
        if a != -1 and b != -1:
            mst.add_branch_to_mst((a, b), min)
            edge_count += 1
            inside[b] = inside[a] = True
    return mst


if __name__ == '__main__':
    doctest.testmod()
