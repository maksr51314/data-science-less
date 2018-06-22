import threading

a = 0
l = threading.Lock()


def hello():
    global a
    for i in range(250000):
        # l.acquire()
        a += 1
        # l.release()


ts = []

for i in range(4):
    t = threading.Thread(target=hello)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print(a)
