def getListItem(l:list, ind:list):
    if len(ind) == 1:
        return l[ind[0]]
    else:
        return getListItem(l[ind[0]], ind[1:])


class MultiArray(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def __getitem__(self, ind):
        if len(str(ind)) == 1:
            return super(MultiArray, self).__getitem__(ind)
        else:
            ind = list(ind)
            return getListItem(super(MultiArray, self).__getitem__(ind[0]), ind[1:])


x = MultiArray([[[91, 42, 56], [19, 14, 15]], [[1, 2, 3], [9, 4, 2]], [[11, 47, 53], [85, 21, 35]]])
print(x[1])
print(x[1, 1])
print(x[1, 1, 2])
print(x.pop(2))
