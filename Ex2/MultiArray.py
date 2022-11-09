class MultiArray(list):

    def __init__(self, *args):
        super().__init__()
        self.l = args

    def __getitem__(self, item):
        if len(item) == 1:
            return self.l[item]
        try:
            return self.l[item[0]][item[1]][item[2]]
        except:
            print("err")


x = MultiArray([[1, 2, 3], [1, 2, 5]])
print(x[0,1,2])
