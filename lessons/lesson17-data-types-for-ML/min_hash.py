import random

N = 50
K = 20


def generate_document():
    return [random.randint(0, N) for i in range(K)]


hashs = [generate_document() for i in range(5)]


def hash_min(hash_, a):
    return min(hash_(s) for s in a)


def minhash(a, b):
    c = 0
    for hash_ in hashs:
        if hash_min(hash_, a) == hash_min(hash_, b):
            c += 1
    return c / 5


def jaccard(a, b):
    return len(set(a) & set(b)) / len(set(a) | set(b))


a = generate_document()
b = generate_document()

print(jaccard(a, b), minhash(a, b))
