# itertools.groupby(iterable, key=None)
class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def __next__(self):
        while self.currkey == self.tgtkey:  # 刚开始，这个２者是相同的均是object()对象
            self.currvalue = next(self.it)  # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))

    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)  # 当迭代到B时，退出这个函数，而且第１６行，也是无法进入while循环的


if __name__ == "__main__":
    for k, g in groupby('AAAABBBCCDAABBB'):
        print(k, list(g))
    # print(list(k for k, g in groupby('AAAABBBCCDAABBB')))
