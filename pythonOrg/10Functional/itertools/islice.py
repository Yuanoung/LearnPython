# itertools.islice(iterable, start, stop[, step])
import sys


def islice(iterable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(*args)
    it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
    try:
        nexti = next(it)
    except StopIteration:
        return
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)


def islice1(iterable, *args):
    s = slice(*args)
    for i in range(s.start or 0, s.stop or sys.maxsize, s.step or 1):
        yield iterable[i]


if __name__ == "__main__":
    print(list(islice1('ABCDEFG', 2, 4)))
