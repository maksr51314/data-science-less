import functools

def add(x, y):
    return x + y

inc = functools.partial(add, 1)


res = inc(2)

print(res)
