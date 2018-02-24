import collections


def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]

    def gen(mydeque):
        while True:
            if not mydeque:  # when the local deque is empty
                try:
                    newval = next(it)  # fetch a new value and
                except StopIteration:
                    return
                for d in deques:  # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()

    return tuple(gen(d) for d in deques)


if __name__ == "__main__":
    for t in tee(range(5), 2):
        print(list(t))
