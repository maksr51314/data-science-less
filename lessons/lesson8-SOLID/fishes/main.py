from Pool import Pool
from Configuration import Configuration
from Vegan import Vegan
from Eater import Eater


class Main:
    def __init__(self):
        self.pool = Pool

        for fish_type, count in (
            (Eater, Configuration.EATER_COUNT),
            (Vegan, Configuration.VEGAN_COUNT)):
            for i in range(count):
                self.pool.add_creature(fish_type)

    def go(self):
        print(self.pool)


main = Main()
main.go()
