import multiprocessing

a = 0


def f():
    global a
    for i in range(100000):
        a += 1


def hello():
    print('Hello')
    for i in range(1000000):
        for j in range(1000):
            pass

ps = []

for i in range(10):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)


for p in ps:
    p.join()

print(a)