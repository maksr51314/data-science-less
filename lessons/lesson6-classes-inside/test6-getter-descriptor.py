class Square:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @property
    def volume(self):
        return self.a * self.b *self.c


square = Square(2, 3, 4)

print(square.volume)
