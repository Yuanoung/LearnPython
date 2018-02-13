# itertools.filterfalse(predicate, iterable)
def filterfalse1(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    return (v for v in range(10) if not predicate(v))


def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


if __name__ == "__main__":
    print(list(filterfalse(lambda x: x % 2, range(10))))
