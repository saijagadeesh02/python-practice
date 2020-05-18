
class Stack(object):

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

class Queue(object):

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class Dequeue(object):

    def __init__(self):
        self.dequeue = []

    def isEmpty(self):
        return self.dequeue == []

    def addFront(self, item):
        self.dequeue.insert(0, item)

    def addRear(self, item):
        self.dequeue.append(item)

    def popFront(self):
        return self.dequeue.pop(0)

    def popRear(self):
        return self.dequeue.pop()

    def size(self):
        return len(self.dequeue)


s = Queue()
s.push(1)
s.push(2)
s.push(3)
print(s.size())
# print(s.peek())
print(s.pop())
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.isEmpty())



