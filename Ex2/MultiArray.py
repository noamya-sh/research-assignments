class MultiArray(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def __getitem__(self, item):
        if len(str(item)) == 1:
            return super(MultiArray, self).__getitem__(item)
        try:
            if len(item) == 2:
                return super(MultiArray, self).__getitem__(item[0])[item[1]]
            if len(item) == 3:
                return super(MultiArray, self).__getitem__(item[0])[item[1]][item[2]]
        except:
            print("err")


x = MultiArray([[[91, 42, 56], [19, 14, 15]], [[1, 2, 3], [9, 4, 2]], [[11, 47, 53], [85, 21, 35]]])
print(x[1])
print(x[1, 1])
print(x[1, 1, 2])
print(x.pop(2))
