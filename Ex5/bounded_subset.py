import doctest
from itertools import chain
from typing import List

def comb(iterable, r, c):
    """
    this is combination gemerator from python docs,
    with slight changes so that a subgroup will be
    created only if it is less than or equal to the
    third argument in the function - C

    """
    # my addition: remove unnecessary elements
    so = sorted(iterable)
    new= list(iterable)
    if r > 1:
        while r < len(so) and sum(so[:r - 1]) <= c < sum(so[:r - 1]) + so[-1]:
                new.remove(so[-1])
                so.pop()

    pool = tuple(new)
    n = len(pool)
    if r > n:
        return
    # indices contain indexes that are candidates to be in a new subset.
    indices = list(range(r))
    # my addition: get sum according to indexes in indices
    s = sum(pool[k] for k in indices)
    if s <= c:
        yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1

        # my addition: get sum according to indexes in indices
        s = sum(pool[k] for k in indices)
        if s <= c:
            yield tuple(pool[i] for i in indices)


def bounded_subset(s: List[int], c: int):
    """"
    generator that provides subsets from a list, which are less than or equal to the number C

    >>> for s in bounded_subset([1,2,3,4,5],0): print(s)
    []
    >>> for s in bounded_subset([1,2,3],4): print(s)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    >>> for s in bounded_subset(range(50, 150), 103): print(s)
    []
    [50]
    [51]
    ...
    [103]
    [50, 51]
    [50, 52]
    [50, 53]
    [51, 52]
    >>> for s in bounded_subset([0.2,-4,3.5,2,8],0): print(s)
    []
    [-4]
    [0.2, -4]
    [-4, 3.5]
    [-4, 2]
    [0.2, -4, 3.5]
    [0.2, -4, 2]
    >>> for s in bounded_subset(list(range(90,100))+list(range(920,1000)),1000): print(s)
    []
    [90]
    ...
    [999]
    [90, 91]
    [90, 92]
    ...
    [91, 92, 93, 94, 95, 96, 97, 98, 99]
    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    """
    sortedList = sorted(s)
    for i in range(len(s) + 1):
        # if sum of n-min greater than c, all combinations
        # with n elements will be greater than c
        if sum(sortedList[:i]) > c:
            break

        # get all combination(this generator not really subsets) with i elements
        subsets = comb(s, i, c)
        for subset in subsets:
            yield list(subset)


def bounded_subset_sorted(s: List[int], c: int):
    """
    generator that provides subsets from a list, which are less than or equal to the number C,
    sorted by them sums.
    >>> for s in bounded_subset_sorted([1,2,3,4,5],0): print(s)
    []
    >>> for s in bounded_subset_sorted([1,1,2,2],4): print(s)
    []
    [1]
    [1]
    ...
    [1, 2]
    [2, 2]
    [1, 1, 2]
    [1, 1, 2]
    >>> for s in bounded_subset_sorted(range(50, 150), 103): print(s)
    []
    [50]
    [51]
    ...
    [102]
    [50, 52]
    [103]
    [50, 53]
    [51, 52]
    >>> for s in bounded_subset_sorted([3,2,0,1,0.5], 4): print(s)
    []
    [0]
    [0.5]
    [0, 0.5]
    [1]
    ...
    [2, 0, 1, 0.5]
    [3, 1]
    [3, 0, 1]
    >>> for s in bounded_subset_sorted([0.2,-4,3.5,2,8],0): print(s)
    [-4]
    [0.2, -4]
    [-4, 2]
    [0.2, -4, 2]
    [-4, 3.5]
    [0.2, -4, 3.5]
    []
    >>> for s in bounded_subset_sorted(list(range(90,100))+list(range(920,1000)),1000): print(s)
    []
    [90]
    ...
    [90, 91]
    [90, 92]
    ...
    [998]
    [999]
    """
    sortedList = sorted(s)
    m = len(s)
    # first get maximum number of element that combination of them small or equals to c
    for i in range(len(s) + 1):
        if sum(sortedList[:i]) > c:
            m = i
            break
    # get chain of all combination (generators, not really subsets) up to m elements,
    # than sort them by sum
    subsets = chain.from_iterable(comb(s, i, c) for i in range(m + 1))
    for subset in sorted(subsets, key=sum):
        yield list(subset)


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    # for s in bounded_subset_sorted(list(range(90,100))+list(range(920,1000)),1000):
    #     print(s)