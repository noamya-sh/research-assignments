import doctest


def getListItem(l: list, ind: list):
    """
    A recursive helper function to get elements using a list of indexes
    """
    if len(ind) == 1:
        return l[ind[0]]
    else:
        return getListItem(l[ind[0]], ind[1:])


def setListItem(l: list, ind: list, value):
    """
    A recursive helper function to set elements using a list of indexes
    """
    if len(ind) == 1:
        l.__setitem__(ind[0],value)
    else:
        return setListItem(l[ind[0]], ind[1:],value)


class MultiArray(list):
    """
    A data structure containing a multidimensional list.
    >>> x = MultiArray([[[91, 42, 56], [19, 14, 15]], [[1, 2, 3], [9, 4, 2]], [[11, 47, 53], [85, 21, 35]]])
    >>> x[1]
    [[1, 2, 3], [9, 4, 2]]
    >>> x[1, 1]
    [9, 4, 2]
    >>> x[1, 1, 2]
    2
    >>> x[1,1,2] = 58
    >>> print(x)
    [[[91, 42, 56], [19, 14, 15]], [[1, 2, 3], [9, 4, 58]], [[11, 47, 53], [85, 21, 35]]]
    >>> x[2,0] = [23,41]
    >>> print(x)
    [[[91, 42, 56], [19, 14, 15]], [[1, 2, 3], [9, 4, 58]], [[23, 41], [85, 21, 35]]]
    >>> y = MultiArray([[[[[1],[55]],[[2],[5]]],[[[66],[55]],[[1],[2],[5]]]],
    ... [[[[32],[64],[55]],[[54],[97,42,47],[78]]],[[[14],[22],[13]],[[11],[12],[51]]]]])
    >>> y[1, 0, 1, 1, 2]
    47
    >>> y[0, 0, 0, 0]
    [1]
    >>> z = MultiArray([1,2,3])
    >>> z[1]
    2
    >>> z[1]=5
    >>> z[1]
    5
    """

    def __init__(self, *args):
        # init by father
        list.__init__(self, *args)

    def __getitem__(self, ind):
        # if it is a single index
        if len(str(ind)) == 1:
            return super(MultiArray, self).__getitem__(ind)
        else:
            ind = list(ind)
            # go to helpful recursive function
            return getListItem(super(MultiArray, self).__getitem__(ind[0]), ind[1:])

    def __setitem__(self, key, value):
        # if it is a single index
        if len(str(key)) == 1:
            super(MultiArray, self).__setitem__(key, value)
        else:
            key = list(key)
            # go to helpful recursive function
            setListItem(self[key[0]],key[1:],value)


if __name__ == '__main__':
    doctest.testmod()
