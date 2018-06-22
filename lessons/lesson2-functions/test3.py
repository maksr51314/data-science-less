a = 1


def f():
    a = 22

    def g():
        print(a)
    g()
    print(a)


# f()


def f2():
    a = 2
    print(a)


f2()


def f3():
    global a
    a = 55


f3()
print(a)
