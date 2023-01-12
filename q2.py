class EmptyQueueException(Exception):
    pass

class FullQueueException(Exception):
    pass




class ArrayDeque:
    CAPACITY = 16
    
    def __init__(self):
        self._data = [None] * ArrayDeque.CAPACITY
        self._r = 0
        self._f = 0
        
        
    def __str__(self):
        return self._data.__str__()
    
    def size(self):
        return (self._r - self._f) % self.CAPACITY
    
    def isEmpty(self):
        return self._r == self._f

    def rear(self):
        if self.isEmpty():
            raise EmptyQueueException
        
        return self._data[self._r]
                  
    def front(self):
        if self.isEmpty():
            raise EmptyQueueException
        
        return self._data[self._f]

    def addRear(self, element):
        if self.size() == self.CAPACITY :
            raise FullQueueException
        
        self._data[self._r] = element
        self._r = (self._r + 1) % self.CAPACITY
        
    def removeRear(self):
        if self.isEmpty():
            raise EmptyQueueException

        value = self._data[self._r]
        self._data[self._r - 1] = None
        self._r = (self._r - 1) % self.CAPACITY
        return value

    def addFront(self, element):
        if self.size == self.CAPACITY:
            raise FullQueueException
        self._f = (self._f - 1) % self.CAPACITY
        self._data[self._f] = element

    def removeFront(self):
        if self.isEmpty():
            raise EmptyQueueException

        value = self._data[self._f]
        self._data[self._f] = None
        self._f = (self._f + 1) % self.CAPACITY
        return value


def check_palindrome_deque(S):
    aq = ArrayDeque()
    if aq.size() == 0:
        raise EmptyQueueException
    else:
        while aq.size() > 1:
            if aq.removeRear() != aq.removeFront:
                return False
            else:
                return True
