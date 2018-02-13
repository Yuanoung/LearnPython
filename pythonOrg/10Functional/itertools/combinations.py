# itertools.combinations(iterable, r)


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:  # 这个语句，如果for没有break则一定会执行
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


if __name__ == "__main__":
    print(list(combinations('ABC', 2)))
    # print(list(combinations(range(4), 3)))
    # nums = [1, 2]
    # for i in nums:
    #     print(i)
    #     break
    # else:
    #     print("empty array")
