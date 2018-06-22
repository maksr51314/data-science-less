class A:
    def __init__(self):
        self.aaa = 1

    def sum(self):
        return self.aaa


class B(A):
    def __init__(self):
        self.bbb = 2
        super().__init__()

    def sum(self):
        return super().sum() + self.bbb


b = B()

print(b.sum())
