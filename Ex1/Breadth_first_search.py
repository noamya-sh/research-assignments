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
                queue.append((neighbor,path_node + [neighbor]))
                visited[neighbor] = True
                if neighbor == end:
                    return path_node + [neighbor]
    return []
