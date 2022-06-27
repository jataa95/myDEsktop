class Fib:
    def __init__(self, n):
        print('__init__')
        self.n = n
        self.i = 0
        self.p1 = self.p2 = 1

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        if self.i in [1, 2]:
            return 1
        ret = self.p1 + self.p2
        self.p1, self.p2 = self.p2, ret
        return ret


for i in Fib(5):
    print(i)
