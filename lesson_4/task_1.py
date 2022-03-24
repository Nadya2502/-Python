class MinStack(object):

    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.insert(0, val)

    def pop(self):
        return self.items.pop(0)

    def top(self):
        return self.items[0]

    def getMin(self):
        return min(self.items)