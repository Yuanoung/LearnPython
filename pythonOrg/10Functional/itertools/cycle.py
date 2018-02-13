# itertools.cycle(iterable)
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:  # 如果这里不用saved，而直接为True，那么如果iterable为空
        for element in saved:
            yield element


def cycle1(iterable):
    if not iterable:
        return
    while True:
        for element in iterable:
            yield element
