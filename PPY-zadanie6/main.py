class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def __str__(self):
        return str(self.list)


    def get(self, e):
        if e in self.list:
            return e
        else:
            return None


    def delete(self, e):
        if e in self.list:
            self.list.rempve(e)


def append(self, e, func=None):
    if func is None:
        self.items.append(e)
        self.items.sort()
    else:
        self.items.append(e)
        self.items.sort(key=func)
