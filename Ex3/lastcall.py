from typing import Callable,List
import doctest

def lastcall(func: Callable):
    """
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
    ... def g(s:str):
    ...     ans = ""
    ...     for i in s:
    ...         ans+=i*2
    ...     return ans
    >>> g("dog")
    'ddoogg'
    >>> g("dog")
    I already told you that the answer is ddoogg
    """

    dic = {}

    def warpper(*args, **kwargs):
        if args:
            arguments = args
        elif kwargs:
            arguments = kwargs
        else:
            raise ValueError("there is no argument")

        if func in dic and arguments in dic[func]:
            print(f'I already told you that the answer is {dic[func][arguments]}')
        else:
            if func not in dic:
                dic.setdefault(func,{})

            val = func(*args, **kwargs)
            dic[func][arguments] = val
            return val

    return warpper

if __name__ == "__main__":
    doctest.testmod()