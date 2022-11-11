from typing import Callable


def lastcall(func: Callable):
    dic = {}

    def warpper(*args, **kwargs):
        if args:
            arguments = args
        elif kwargs:
            arguments = kwargs
        else:
            raise ValueError("there is no argument")
        if len(arguments) > 1:
            raise ValueError("only one argument")

        if dic[(func, arguments)]:
            print(f'I already told you that the answer is {dic[(func, arguments)]}')
        else:
            val = func(*args, **kwargs)
            dic[(func, arguments)] = val
        return val

    return warpper


@lastcall
def f(x: int):
    return x ** 2


f(2)
f(2)