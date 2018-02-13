# itertools.dropwhile(predicate, iterable)
def dropwhile1(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    for i in range(len(iterable)):
        if not predicate(iterable[i]):
            break
    return iterable[i:]


def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)  # 很容易的使用yield语法
    for x in iterable:
        if not predicate(x):
            yield x  # 这里已经调用了一次next了，所以如果该值不满足条件后，应该要将其返回
            break
    for x in iterable:
        yield x


if __name__ == "__main__":
    print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))
