import threading
import time
import random

N = 5
countNum = 0
forks = [threading.Lock() for i in range(N)]
buffer_semaphore = threading.Semaphore(value=N-2)


def right(i):
    return i


def left(i):
    return (i + 1) % N


def philosopther(i):

    while True:
        print(i, ' thinking')
        time.sleep(1/random.randint(80000, 100000))
        # buffer_semaphore.acquire()

        forks[min(left(i), right(i))].acquire()
        forks[max(left(i), right(i))].acquire()
        # forks[left(i)].acquire()
        # forks[right(i)].acquire()
        print(i, ' eating', countNum)
        time.sleep(1/random.randint(30000, 150000))
        forks[left(i)].release()
        forks[right(i)].release()


for i in range(N):
    t = threading.Thread(target=philosopther, args=(i,))

    # buffer_semaphore.release()
    t.start()

t.join()
