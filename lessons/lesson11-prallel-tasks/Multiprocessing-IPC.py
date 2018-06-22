import multiprocessing

PROCESS_COUNT = 40

a = 0
q = multiprocessing.Queue()


def f():
    global a
    for i in range(100000):
        a += 1
    q.put(a)


ps = []

for i in range(PROCESS_COUNT):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)

# for p in ps:
#     p.join()

for i in range(PROCESS_COUNT):
    a += q.get()

print(a)
