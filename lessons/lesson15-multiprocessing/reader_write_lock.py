import threading
import random
import time

readers_lock = threading.Lock()
can_write = threading.Lock()
readers_number = 0

def reader(i):
    global readers_number
    while True:
        with readers_lock:
            if readers_number == 0:
                can_write.acquire()
            readers_number += 1
        print('Reader ', i, ' starts reading')
        time.sleep(random.randint(1,5))
        print('Reader ', i, ' ends reading')

        with readers_lock:
            readers_number -= 1
            if readers_number == 0:
                can_write.release()

def write(i):
    while True:
        with can_write:
            print('Writer ', i, ' starts reading')
            time.sleep(random.randint(1, 5))
            print('Writer ', i, ' ends reading')

for i in range(1, 5):
    t = threading.Thread(target=reader, args=(i,))
    t.start()
    t = threading.Thread(target=write, args=(i,))
    t.start()


# Not neee
# t.join()
