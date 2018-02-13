# itertools.accumulate(iterable[, func])
# func必须能够接受2个参数

import operator
from itertools import repeat


def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    # 这里如果就用一个for循环来表示的话，因为需要返回第一个元素，所以很不优雅。
    it = iter(iterable)  # 返回一个迭代器
    try:
        total = next(it)  # 这里可能是一个空的
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


if __name__ == "__main__":
    data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    print(list(accumulate(data, operator.mul)))  # running product

    print(list(accumulate(data, max)))  # running maximum

    cashflows = [1000, -90, -90, -90, -90]
    print(list(accumulate(cashflows, lambda bal, pmt: bal * 1.05 + pmt)))

    logistic_map = lambda x, _: r * x * (1 - x)
    r = 3.8
    x0 = 0.4
    inputs = repeat(x0, 36)  # only the initial value is used
    print([format(x, '.2f') for x in accumulate(inputs, logistic_map)])
