import doctest
from itertools import combinations, chain
from typing import List


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
    """
    s = sorted(s)
    for i in range(len(s) + 1):
        # if sum of n-min greater than c, all combinations
        # with n elements will be greater than c
        if sum(s[:i]) > c:
            break

        # get all combination with i elements
        subsets = combinations(s, i)
        for subset in subsets:
            if sum(subset) <= c:
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
    """
    s = sorted(s)
    m = len(s)
    # first get maximum number of element that combination of them small or equals to c
    for i in range(len(s) + 1):
        if sum(s[:i]) > c:
            m = i
            break
    # get chain of all combination up to m elements,
    # than sort them by sum
    subsets = chain.from_iterable(combinations(s, i) for i in range(m + 1))
    for subset in sorted(subsets, key=sum):
        if sum(subset) <= c:
            yield list(subset)


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.ELLIPSIS)
