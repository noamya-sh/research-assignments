import doctest


def f(a: int, b: str, c: float,d):
    annotations = f.__annotations__
    vars = locals()
    print(vars)
    for x in annotations.keys():
        if annotations[x] is not type(vars[x]):
            raise ValueError()

    print('~~~~~~~~~~~')


f(1, "kk",2.2,5)
