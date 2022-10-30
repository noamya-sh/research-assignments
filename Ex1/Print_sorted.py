def print_sorted(x):
    list =[]
    for i in enumerate(x):
        list.append(str(i))
    list.sort()
    print(list)


print_sorted([4, {'a': "v", 'c': [2]}, (1, 3,2, 3)])
