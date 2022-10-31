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
        return str(sorted(output_dict))
    else:
        output_list = []
        for i in struct:
            if type(i) in [list, dict, tuple, set]:
                output_list.append(helpi(i))
            else:
                output_list.append(str(i))
        return str(sorted(input_class(output_list)))


#
# def f(struct):
#     for i in struct:
#         if type(i) in [list, dict, tuple, set]:
#             return f(i)
#     return str(struct)
#
# # print_sorted([4, {'a': "v", 'c': [2]}, (1, 3,2, 3)])
r = [4, [9, 7], {'d': "v", 'c': [2]}, (1, 3, 2, 3), 5]
print(helpi(r))
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
