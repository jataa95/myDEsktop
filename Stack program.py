class Stack:
    def __init__(self):
        self.stk = []

    def push(self, val):
        self.stk.append(val)

    def pop(self):
        val = self.stk[-1]
        del self.stk[-1]
        return val


class countStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def pop(self):
        self.counter += 1
        return super().pop()

    def getCounter(self):
        return self.counter


obj = countStack()
for i in range(100):
    obj.push(i)
    obj.pop()
print(obj.getCounter())
