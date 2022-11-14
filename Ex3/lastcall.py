from typing import Callable
import doctest

def lastcall(func: Callable):
    """
    >>> @lastcall
    ... def k(s: str):
    ...     return s*2
    >>> k("Good")
    'GoodGood'
    >>> k("Good")
    I already told you that the answer is GoodGood
    >>> k(5)
    10
    >>> k(5)
    I already told you that the answer is 10
    """

    dic = {}

    def warpper(*args, **kwargs):
        if args:
            arguments = args
        elif kwargs:
            arguments = kwargs
        # else:
        #     raise ValueError("there is no argument")
        # if len(str(arguments)) > 1:
        #     raise ValueError("only one argument")

        if func in dic and arguments in dic[func]:
            print(f'I already told you that the answer is {dic[func][arguments]}')
        else:
            if func not in dic:
                dic.setdefault(func,{})

            val = func(*args, **kwargs)
            dic[func][arguments] = val
            return val

    return warpper


@lastcall
def f(x: int):
    return x ** 2


if __name__ == "__main__":
    doctest.testmod()