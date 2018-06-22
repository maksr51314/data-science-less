def coroutine(f):
    g = f()
    next(g)
    return g


def main():
    i = f.send(0)
    print('main', i)
    i = f.send(i + 1)
    print('main', i)
    i = f.send(i + 1)
    print('main', i)

@coroutine
def f():
    i = yield
    print('f()', i)
    i = yield i + 1
    print('f()', i)
    i = yield i + 1
    print('f()', i)
    i = yield i + 1


main()
