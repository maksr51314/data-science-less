import random

limits = [1_000_000 // (2**i) for i in range(0, 19) if 1_000_000 // (2**i) > 400]

# print(limits)
# random.randint(0, 1_000_000)

for i in range(1000):
    r = random.randint(0, 1_000_000)
    for high, low in zip(limits[:-1], limits[1:]):
        # print(low, high)
        if low < r < high:
            print(low)
            break
        else:
            print(r)