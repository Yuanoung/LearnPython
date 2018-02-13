# itertools.compress(data, selectors)


def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in zip(data, selectors) if s)


if __name__ == "__main__":
    print(list(compress('ABCDEF', [1, 0, 1, 0, 1, 1])))
