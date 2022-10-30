

from typing import Callable

"""Return the factorial of n, an exact integer >= 0.
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000
    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

def safe_call(func: Callable,*args,**kwargs):
    annotations = func.__annotations__
    print(func.__annotations__)
    if args:
        list = locals()['args']
        vars ={}
        i = 0
        for k in annotations.keys():
            vars[k] = list[i]
            i+=1
        print("args", vars)
    else:
        vars = locals()['kwargs']
    print("vars",vars)
    for x in annotations.keys():
        if annotations[x] is not type(vars[x]):

            raise ValueError("ERROR")

    print('~~~~~~~~~~~')


def f(y: float, x: int, z = 5):
    return x + y + z


safe_call(f,2.3,1,6)
