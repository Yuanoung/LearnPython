""" Example adapted from ``yield_delegate_fail.py``

The following program performs a simple abstraction over the process of
yielding.

"""


# BEGIN YIELD_DELEGATE_FIX
def f():
    def do_yield(n):
        yield n

    x = 0
    while True:
        x += 1
        yield from do_yield(x)  # 可以驱动do_yield，而不用显示的初始化．


def f1():
    def do_yield(n):
        yield n

    x = 0

    while True:
        x += 1
        try:
            yield next(do_yield(x))
        except StopIteration:
            continue


# END YIELD_DELEGATE_FIX

if __name__ == '__main__':
    print('Invoking f() now produces a generator')
    g = f1()
    print(next(g))
    print(next(g))
    print(next(g))
