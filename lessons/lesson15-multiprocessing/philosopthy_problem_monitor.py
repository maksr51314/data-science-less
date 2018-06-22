import threading
import time
import random

N = 5

# Stages = {'hungry','thinking','eating'}

THINKING, HUNGRY, EATING = range(3)


class Philosopher:
    def __init__(self, i):
        self.state = THINKING
        self.i = i
        self.c = threading.Condition()

    def thinking(self):
        self.state = THINKING
        print(i, 'thinking')
        time.sleep(1/random.randint(90000, 1000000))

    def eating(self):
        self.state = EATING
        print(i, 'eating')
        time.sleep(1 / random.randint(40000, 60000))

    def right(self):
        return (self.i - 1 + N) % N

    def left(self):
        return (self.i + 1) % N

    def take_forks(self):
        self.state = HUNGRY
        with self.c:
            while philosophers[self.left()].state == EATING or \
                philosophers[self.right()].state == EATING:
                self.c.wait()

    def put_forks(self):
        if philosophers[self.left()].state == HUNGRY: # and \
                # philosophers[philosophers[self.left()].left()].state != EATING:
            with philosophers[self.left()].c:
                philosophers[self.left()].c.notify()

        if philosophers[self.right()].state == HUNGRY:
            with philosophers[self.right()].c:
                philosophers[self.right()].c.notify()

philosophers = [Philosopher(i) for i in range(N)]


def life_circle(i):
    while True:
        philosophers[i].thinking()
        philosophers[i].take_forks()
        philosophers[i].eating()
        philosophers[i].put_forks()


for i in range(N):
    t = threading.Thread(target=life_circle, args=(i,))
    t.start()

t.join()
