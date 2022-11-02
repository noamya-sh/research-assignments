import doctest

from typing import Callable


def Breadth_first_search(start: tuple, end: tuple, neighbor_function: Callable) -> list:
    """Get path from 'start' node to 'end' node by neighbor function.
            >>> def n(node: tuple):
            ...     x, y = node
            ...     return [(x, y - 1), (x + 1, y), (x - 1, y), (x, y + 1)]
            >>>
            >>> Breadth_first_search((1,1),(3,2),n)
            [(1, 1), (2, 1), (3, 1), (3, 2)]
            >>> Breadth_first_search((5,7),(2,1),n)
            [(5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1)]
            >>> def k(node: tuple):
            ...     x, y = node
            ...     return [ (x, y + 1),(x + 1, y),(x, y - 1), (x - 1, y)]
            >>> Breadth_first_search((1,1),(3,2),k)
            [(1, 1), (1, 2), (2, 2), (3, 2)]
            >>> def g(node: tuple):
            ...     x, y, z = node
            ...     return [(x, y - 1,z), (x, y ,z -1), (x -1, y ,z), (x, y + 1, z),
            ... (x +1, y ,z),(x , y ,z +1)]
            >>> Breadth_first_search((1,1,2),(3,1,2),g)
            [(1, 1, 2), (2, 1, 2), (3, 1, 2)]
            >>> Breadth_first_search((5,8,2),(5,8,2),g)
            []
            """
    if start == end:
        return []

    # perform bfs
    visited = {start: True}  # for prevent cycle
    queue = [(start, [start])]  # init with node and path
    while queue:
        node, path_node = queue.pop(0)
        neighbor_list = neighbor_function(node)  # function given in input
        for neighbor in neighbor_list:
            if neighbor not in visited:
                if neighbor == end:
                    return path_node + [neighbor]
                queue.append((neighbor, path_node + [neighbor]))
                visited[neighbor] = True

    return []


if __name__ == "__main__":
    doctest.testmod()
