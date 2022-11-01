import Empty

class ArrayDequeue:
    ''' FIFO dequeue implementation using a Python list as underlying storage. '''
    DEFAULT_SIZE = 10
    def __init__(self) -> None:
        self._data = [None] * ArrayDequeue.DEFAULT_SIZE
        self._first = 0
        self._size = 0

    def len(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")

        return self._data[self._first]
    
    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        
        return self._data[(self._first + self._size - 1) % len(self._data)]

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(self._size * 2)
        
        self._first = (self._first - 1) % len(self._data)
        self._data[self._first] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(self._size * 2)

        self._data[(self._first + self._size) % len(self._data)] = e
        self._size += 1
        

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        e = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        
        return e

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        last = (self._first + self._size - 1) % len(self._data)
        e = self._data[last]
        self._data[last] = None
        self._size -= 1
        
        return e


    def _resize(self, new_size):
        old = self._data
        self._data = [None] * new_size
 
        for i in range(self._size):
            self._data[i] = old[(self._first + i) % len(old)]

        self._front = 0

def usage():
    q = ArrayDequeue()
    print(q.len())
    print(q.is_empty())
    q.add_last(1)
    q.add_last(2)
    q.add_last(3)
    print(q._data)
    q.add_first(4)
    print(q.delete_last())
    q.add_first(5)
    print(q._data)
    print(q._first)

if __name__ == "__main__":
    usage()