import doctest
from typing import Callable

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
        # If a change in input type is found
        if annotations[x] is not type(vars[x]):
            raise ValueError("Annotation does not match")

if __name__ == "__main__":
    doctest.testmod()
