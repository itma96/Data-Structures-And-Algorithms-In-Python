from solutions.ch6.Empty import Empty

class ArrayQueue:
    ''' FIFO queue implementation using a Python list as underlying storage. '''
    DEFAULT_SIZE = 3

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_SIZE
        self._front = 0
        self._size = 0

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(self._size * 2)

        self._data[(self._front + self._size) % len(self._data)] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return e

    def _resize(self, new_size):
        old = self._data
        self._data = [None] * new_size
 
        for i in range(self._size):
            self._data[i] = old[(self._front + i) % len(old)]

        self._front = 0

def usage():
    q = ArrayQueue()
    print(q.len())
    print(q.is_empty())
    q.enqueue(3)
    print(q.is_empty())
    q.enqueue(5)
    print(q.len())
    print(q._data)
    print(q.dequeue())
    print(q._data)
    print(q.dequeue())
    print(q._data)
    q.enqueue(4)
    print(q._data)
    q.enqueue(5)
    print(q._data)
    q.enqueue(7)
    print(q._data)
    print(q.dequeue())
    q.enqueue(9)
    print(q._data)
    q.enqueue(11)
    print(q._data)
    print(q._front)
    print(q._size)

if __name__ == "__main__":
    usage()