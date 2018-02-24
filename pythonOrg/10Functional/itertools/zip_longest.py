from itertools import repeat, chain


class ZipExhausted(Exception):
    pass


def zip_longest(*args, **kwds):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = len(args) - 1

    def sentinel():
        nonlocal counter  # 因为在该函数中，下面有语句对counter进行赋值，所以15行会报错，而不是将counter视为外层函数中的zip_longest
        if not counter:
            raise ZipExhausted
        counter -= 1
        yield fillvalue

    fillers = repeat(fillvalue)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    try:
        while iterators:
            _ = tuple(map(next, iterators))
            yield _
    except ZipExhausted:
        pass


z = zip_longest('ABCD', 'xy', fillvalue='-')
print(list(z))
