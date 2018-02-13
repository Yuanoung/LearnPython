# itertools.chain(*iterables)


def chain(*iterables):  # 这里主要是有个*号
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
