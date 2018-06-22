class Line:
    def __init__(self):
        self._l = 0

    @property
    def length(self):
        return self._l * 4

    @length.setter
    def length(self, val):
        self._l = val / 4


line = Line()

line.length = 100
print(line.length)
print(line._l)

line.length = 200
print(line.length)
print(line._l)