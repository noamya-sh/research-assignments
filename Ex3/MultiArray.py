import doctest


def getListItem(l:list, ind:list):
    if len(ind) == 1:
        return l[ind[0]]
    else:
        return getListItem(l[ind[0]], ind[1:])


class MultiArray(list):
    """
    >>> x = MultiArray([[[91, 42, 56], [19, 14, 15]], [[1, 2, 3], [9, 4, 2]], [[11, 47, 53], [85, 21, 35]]])
    >>> x[1]
    [[1, 2, 3], [9, 4, 2]]
    >>> x[1, 1]
    [9, 4, 2]
    >>> x[1, 1, 2]
    2
    >>> y = MultiArray([[[[[1],[55]],[[2],[5]]],[[[66],[55]],[[1],[2],[5]]]],
    ... [[[[32],[64],[55]],[[54],[97,42,47],[78]]],[[[14],[22],[13]],[[11],[12],[51]]]]])
    >>> y[1, 0, 1, 1, 2]
    47
    >>> y[0, 0, 0, 0]
    [1]
    """
    def __init__(self, *args):
        list.__init__(self, *args)

    def __getitem__(self, ind):
        if len(str(ind)) == 1:
            return super(MultiArray, self).__getitem__(ind)
        else:
            ind = list(ind)
            return getListItem(super(MultiArray, self).__getitem__(ind[0]), ind[1:])


if __name__ == '__main__':
    doctest.testmod()