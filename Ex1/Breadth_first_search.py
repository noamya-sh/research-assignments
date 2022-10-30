import doctest

from typing import Callable


def Breadth_first_search(start: tuple, end: tuple, neighbor_function: Callable) -> list:
    visited = {start: True}
    queue = [(start, [start])]
    while queue:
        node, path_node = queue.pop(0)
        neighbor_list = neighbor_function(node)
        for neighbor in neighbor_list:
            if neighbor not in visited:
                if neighbor == end:
                    return path_node + [neighbor]
                queue.append((neighbor, path_node + [neighbor]))
                visited[neighbor] = True

    return []


g = []
for i in range(10):
    for j in range(10):
        g.append((i, j))


def n(node: tuple):
    x, y = node
    return [(x, y - 1), (x + 1, y), (x - 1, y), (x, y + 1)]


print(Breadth_first_search((0, 0), (3, 1), n))
