import threading
import collections
import random
import time

buffer = collections.deque(maxlen=5)
is_full_semaphore = threading.Semaphore(value=5)
is_empty_semaphore = threading.Semaphore(value=0)

def producer():
    while True:
        mess = random.randint(1, 10)
        print("P: ", mess)
        is_full_semaphore.acquire()
        buffer.appendleft(mess)
        print('LENGTH: ', len(buffer))
        is_empty_semaphore.release()
        time.sleep(random.randint(1, 4))


def consumer():
    while True:
        is_empty_semaphore.acquire()
        mess = buffer.pop()
        is_full_semaphore.release()
        print("C: ", mess)
        print('LENGTH: ', len(buffer))
        time.sleep(random.randint(1, 10))

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()

p.join()
