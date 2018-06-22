import itertools


def filter_deviders(items, n):
    for item in items:
        if item % n != 0:
            yield item


def get_primes():
    items = itertools.count(2)
    while True:
        prime = next(items)
        items = filter_deviders(items, prime)
        yield prime


# a = list(itertools.islice(get_primes(), 950))

# print(a)

print(list(itertools.product(['a', 'b'], repeat=2)))
