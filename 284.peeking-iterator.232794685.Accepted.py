class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.n = None

    def peek(self):
        if self.n == None:
            self.n = self.iterator.next()
        return self.n

    def next(self):
        if self.n != None:
            tmp = self.n
            self.n = None
            return tmp
        else:
            return self.iterator.next()

    def hasNext(self):
        if self.n != None:
            return True
        else:
            return self.iterator.hasNext()
