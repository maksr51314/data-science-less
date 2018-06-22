import multiprocessing


def f(x):
    return x * x


p = multiprocessing.Pool(5)
a = p.map(f, range(100))

print(a)
