import doctest
from typing import Callable

"""Checks if the arguments match the annotations of the given function..
    >>> def f(y: float, x: int, z=5):
            return x + y + z
    >>> as
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


def safe_call(func: Callable, *args, **kwargs):
    """Checks if the arguments match the annotations of the given function.
        >>> def f(y: float, x: int, z=5): return x + y + z
        >>> safe_call(f,2,1,7)
        Traceback (most recent call last):
            ...
        ValueError: Annotation does not match
        >>> safe_call(f,"fff",3,6)
        Traceback (most recent call last):
            ...
        ValueError: Annotation does not match
        >>> safe_call(f,2)
        Traceback (most recent call last):
            ...
        ValueError: Arguments are missing
        >>> safe_call(f,2.5,1,7)
        >>> def k(a: list, b: tuple, c:float): return 2
        >>> safe_call(k,[2,3],(1,9,0),7.2)
        >>> safe_call(k,(1,"j",0),[1,15],2.1)
        Traceback (most recent call last):
            ...
        ValueError: Annotation does not match
        >>> safe_call(k,2)
        Traceback (most recent call last):
            ...
        ValueError: Arguments are missing
        """

    # get annotations of given function
    annotations = func.__annotations__
    # get arguments types
    if args:
        l = locals()['args']
        vars = dict(zip(list(annotations.keys()), l))
    else:
        vars = locals()['kwargs']
    # throw exception if arguments are missing
    if len(vars) < len(annotations):
        raise ValueError("Arguments are missing")

    for x in annotations.keys():
        if annotations[x] is not type(vars[x]):
            raise ValueError("Annotation does not match")


def f(y: float, x: int, z=5):
    return x + y + z


safe_call(f, 2.3, 1, 6)
