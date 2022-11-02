# import json
#
#
# def print_sorted(x):
#     list = []
#     for i in enumerate(x):
#         list.append(str(i))
#     list.sort()
#     print(list)
#
def helpi(struct):
    input_class = type(struct)
    if input_class == dict:
        output_dict = {}
        for k, v in struct.items():
            if type(k) in [list, dict, tuple, set]:
                if type(v) in [list, dict, tuple, set]:
                    output_dict[helpi(k)] = helpi(v)
                else:
                    output_dict[helpi(k)] = str(v)
            else:
                if type(v) in [list, dict, tuple, set]:
                    output_dict[str(k)] = helpi(v)
                else:
                    output_dict[str(k)] = str(v)
        print("aa", {i[0]: i[1] for i in sorted(output_dict.items())})
        print("bb", str({i[0]: i[1] for i in sorted(output_dict.items())}))
        return str({i[0]: i[1] for i in sorted(output_dict.items())})
    else:
        output_list = []
        for i in struct:
            if type(i) in [list, dict, tuple, set]:
                output_list.append(helpi(i))
            else:
                output_list.append(str(i))
        return str(input_class(sorted(output_list)))


#
# def f(struct):
#     for i in struct:
#         if type(i) in [list, dict, tuple, set]:
#             return f(i)
#     return str(struct)
#
# # print_sorted([4, {'a': "v", 'c': [2]}, (1, 3,2, 3)])
# input_class = type((2,1,3))
# output_list = [2,1,3]
# print(input_class(sorted(output_list)))

r = [{5: 'v', 7: [2]}, "ss", 4, [9, 7], (1, 3, 2, 3), 5]
print(helpi(r))

# c = {'c':2,'a':[5,1,2]}
#
# x = str({str(i[0]):str(i[1]) for i in sorted(c.items())})
# print(x)
# k = []
# for i in r:
#     if type(i) in [list, dict, tuple, set]:
#         k.append(str(sorted(i)))
#     else:
#         k.append(str(i))
# k.sort()
# print(k)
# # helpi(r)
# # print(sorted(r))
"1 2 3 4 5 6 7 8 9" \
"4 5 6 7 8 9 1 2 3" \
"7 8 9 1 2 3 4 5 6" \
"9 1 2 3 4 5 6 7 8" \
"3 4 5 6 7 8 9 1 2" \
"6 7 8 9 1 2 3 4 5" \
"8 9 1 2 3 4 5 6 7" \
"2 3 4 5 6 7 8 9 1" \
"5 6 7 8 9 1 2 3 4"
