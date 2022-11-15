from typing import Callable
import doctest


def lastcall(func: Callable):
    """
    Decorator function to prevent repeated activation of a function on the same input.
    >>> @lastcall
    ... def k(s):
    ...     return s*2
    >>> k("Good")
    'GoodGood'
    >>> k("Good")
    I already told you that the answer is GoodGood
    >>> k(5)
    10
    >>> k(5)
    I already told you that the answer is 10
    >>> @lastcall
    ... def h(t:tuple):
    ...     return t[0]/t[1]
    >>> h((6,2))
    3.0
    >>> h((6,2))
    I already told you that the answer is 3.0
    >>> @lastcall
    ... def g(d:dict):
    ...     ans = ""
    ...     for k,v in d.items():
    ...         ans+=str(k)+":"+str(v)+" "
    ...     return ans
    >>> g({"aba":1,5:6,(1,2,3):4})
    'aba:1 5:6 (1, 2, 3):4 '
    >>> g({"aba":1,5:6,(1,2,3):4})
    I already told you that the answer is aba:1 5:6 (1, 2, 3):4
    """
    # To store the functions and inputs
    dic = {}

    def warpper(*args, **kwargs):
        if args:
            arguments = args
        elif kwargs:
            arguments = kwargs
        else:
            raise ValueError("there is no argument")
        # dict and list not hashable -> convert to str
        if type(arguments[0]) in (dict, list):
            arguments = str(arguments)

        # If the function has already been run on this input
        if func in dic and arguments in dic[func]:
            print(f'I already told you that the answer is {dic[func][arguments]}')
        else:
            if func not in dic:
                dic.setdefault(func, {})

            val = func(*args, **kwargs)
            dic[func][arguments] = val
            return val

    return warpper


if __name__ == "__main__":
    doctest.testmod()
