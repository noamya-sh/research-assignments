import doctest


def print_sorted(struct):
    """Print the data structure sorted (also in depth).
                >>> print_sorted([{5: 'v', 7: [2]}, "ss", 4, [9, 7], (1, 3, 2, 3), 5])
                ["('1', '2', '3', '3')", '4', '5', "['7', '9']", 'ss', '{'5': 'v', '7': "['2']"}']
                >>> print_sorted({(8,7,(9,6, (5,4, (3,2,(1,0)))))})
                {'('('('("('0', '1')", '2', '3')', '4', '5')', '6', '9')', '7', '8')'}
                >>> print_sorted({'A':[9,1,5],(8.2,1,9.7):[8,1,2],'b':{'h':['k',2,"as"]}})
                {"('1', '8.2', '9.7')": "['1', '2', '8']", 'A': "['1', '5', '9']", 'b': '{'h': "['2', 'as', 'k']"}'}
                >>> print_sorted({80,5,[2,1]})
                Traceback (most recent call last):
                    ...
                TypeError: unhashable type: 'list'
                """
    # help function
    print(helpi(struct))


def helpi(struct):
    # To sort lexically, create a new data structure based on the input type.
    input_class = type(struct)
    if input_class == dict:
        output_dict = {}
        # for any key&value perform a recursion to create a sorted string.
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
        # return string of new dict in a sorted manner and without text distortion
        return str({i[0]: i[1] for i in sorted(output_dict.items())}).replace("\\", "")
    else:
        output_list = []
        # for any element perform a recursion to create a sorted string.
        for i in struct:
            if type(i) in [list, dict, tuple, set]:
                output_list.append(helpi(i))
            else:
                output_list.append(str(i))
        # return string of new list in a sorted manner and without text distortion
        return str(input_class(sorted(output_list))).replace("\\", "")

if __name__ == "__main__":
    doctest.testmod()