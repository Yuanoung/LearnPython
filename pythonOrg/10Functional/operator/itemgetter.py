# operator.itemgetter(item)
# operator.itemgetter(*items)

"""
    >>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
    >>> getcount = itemgetter(1)
    >>> list(map(getcount, inventory))  # 如果这里用for循环的话，
    [3, 2, 5, 1]
    >>> sorted(inventory, key=getcount)
    [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

"""


def itemgetter(*items):
    if len(items) == 1:
        item = items[0]

        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g
