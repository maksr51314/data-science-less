import random
import threading
import time

readers_lock = threading.Lock()
writers_lock = threading.Lock()
can_write = threading.Lock()
try_read = threading.Lock()
writers_number = readers_number = 0


def reader(i):
    global readers_number
    while True:
        try_read.acquire()
        with readers_lock:
            if readers_number == 0:
                can_write.acquire()
            readers_number += 1
        try_read.release()
        print('Reader', i, 'start')
        time.sleep(random.randint(1, 2))
        print('Reader', i, 'finish')
        with readers_lock:
            readers_number -= 1
            if readers_number == 0:
                can_write.release()


def writer(i):
    global writers_number
    while True:
        with writers_lock:
            if writers_number == 0:
                try_read.acquire()
            writers_number += 1
        with can_write:
            print('Writer', i, 'start')
            time.sleep(random.randint(1, 5))
            print('Writer', i, 'finish')
        with writers_lock:
            writers_number -= 1
            if writers_number == 0:
                try_read.release()


for i in range(5):
    t = threading.Thread(target=reader, args=(i,))
    t.start()
for i in range(3):
    t = threading.Thread(target=writer, args=(i,))
    t.start()
