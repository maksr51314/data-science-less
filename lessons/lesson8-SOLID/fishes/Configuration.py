import random

Configuration = {
    'EATER_COUNT': 4,
    'VEGAN_COUNT': 3,
    'POOL_SIZE': (10, 10),
    'EATER_TIME_TO_LIVE': 7,
    'VEGAN_TIME_TO_LIVE': 5,
    'TIME_TO_BORN': 4,
    'EATER_NEW': 2
}


class Fish:
    def __init__(self, position):
        self._position = position


class Eater(Fish):
    def __repr__(self):
        return 'P'


class Vegan(Fish):
    def __repr__(self):
        return 'V'

        # def move(self, is_in_bouns_fn):
        #     while True:


class Pool:
    def __init__(self):
        self._pool_size = Configuration['POOL_SIZE']
        self._creatures = []

    def add_creature(self, fish_type):
        x = random.randint(0, self._pool_size[0])
        y = random.randint(0, self._pool_size[1])
        self._creatures.append(fish_type(x, y))

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


class Main:
    def __init__(self):
        self.pool = Pool

        # self.conf = Configuration()
        # print(Configuration)
        for fish_type, count in (
                (Eater, Configuration['EATER_COUNT']),
                (Vegan, Configuration['VEGAN_COUNT'])):
            for i in range(count):
                self.pool.add_creature(fish_type)

    def go(self):
        print(self.pool)


main = Main()
main.go()
