class Queue:

    def __init__(self):
        self.store = []

    def queue(self, value):
        self.store.append(value)

    def dequeue(self):
        self.store.pop(0)

    def viewContents(self):
        for value in self.store:
            print value
