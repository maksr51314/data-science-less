from .Configuration import Configuration
from Eater import Eater
from Vegan import Vegan

import random


class Pool:
    def __init__(self):
        self._pool_size = Configuration.POOL_SIZE
        self._creatures = {}

    def add_creature(self, fish_type):
        x = random.randint(0, self._pool_size[0])
        y = random.randint(0, self._pool_size[1])
        self._creatures[(x, y)] = fish_type(x, y)

    def __repr__(self):
        repr_ = ''
        for x in range(self._pool_size[0]):
            for y in range(self._pool_size[1]):
                if (x, y) in self._creatures:
                    repr_ += repr(self._creatures[(x, y)])
                else:
                    repr_ += '-'
            repr_ += '\n'
        return repr_
