class Stack:
    def __init__(self):
        self.store = []

    def push(self, value):
        self.store.append(value)

    def pop(self):
        self.store.pop()

    def viewContents(self):
        for value in self.store:
            print value

    def peek(self):
        print self.store[len(self.store) - 1]
