"""
The mod module

pydoc test2 without file format
"""


def add(x: int, y: int) -> int:
    """python3 -m doctest test2.py -v
    >>> add(2,3)
    5
    >>> add(-2,-2)
    -4
    # >>> add('2','2')
    # '22'
    """
    return x + y


# print(add(2, 3))


def super_add(x: int = 1, y: int = 2) -> int:
    return x * y


# print(super_add(y=11))


def lot_args(item, *args):
    for i in args:
        item += i
    print(item)
    return item


# lot_args(1, 2, 3, 2)


def lot_named_args(price: int, *, kg: int = None, g: int = None) -> int:
    """

    :rtype: int
    """
    if kg is not None:
        return kg*price
    elif g is not None:
        return g*1000*price


print(lot_named_args(4, kg=20))

# lot_args(1, 2, 3, 2)


def f(a, my_list=[]):
    my_list.append(a)
    print(my_list)

# f(1)
# f(5)


sentinal = object()


def f2(a=sentinal):
    if a is not sentinal:
        return a
    else:
        return 42


print(f2(None))


def f3(a, b, c):
    return a+b+c


my_arguments = (1, 2, 2)

print(f3(*my_arguments))


def f4(x, y):
    return x + y, x * y


print(f4(2, 9))
