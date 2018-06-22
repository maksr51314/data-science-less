import profile
import functools

a = functools.lru_cache()

class Memo:
    def __init__(self):
        self._state = {}

    def __call__(self, f):
        def wrapper(x):
            if x not in self._state:
                self._state[x] = f(x)
            return self._state[x]
        return wrapper



@Memo()
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


a = profile.run('fib(20)')

# print(a)