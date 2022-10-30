import doctest


def safe_call(a: int, b: str, c: float,d):
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

    annotations = safe_call.__annotations__
    vars = locals()
    print(vars)
    for x in annotations.keys():
        if annotations[x] is not type(vars[x]):
            raise ValueError()

    print('~~~~~~~~~~~')


safe_call(1, "kk", 2.2, 5)
