# classmethod chain.from_iterable(iterable)


def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


if __name__ == "__main__":
    print(list(from_iterable(['ABC', 'DEF'])))
    print(list(from_iterable([[1, 2, 3], [4, 5, 6]])))
