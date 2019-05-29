class Deque(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def add_front(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop(0)

    def add_tail(self,item):
        self.items.append(item)

    def remove_tail(self):
        return self.items.pop()

    def size(self):
        return len(self.items)