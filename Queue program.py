class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.q = []

    def put(self, elem):
        self.q.append(elem)

    def get(self):
        elem = self.q[0]
        del self.q[0]
        return elem


class subQueue(Queue):
    def emptyQueue(self):
        return len(self.q) == 0


que = Queue()
que.put(1)
que.put('dog')
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue is empty!")
