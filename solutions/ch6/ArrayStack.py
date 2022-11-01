from solutions.ch6.Empty import Empty

import sys

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage. '''

    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)
    
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def len(self):
        return len(self._data)

def usage():
    s = ArrayStack()

    s.push((1, 2, 3))
    print(s.pop())

    sys.exit()

    s.push(5)
    s.push(3)
    print(s.len())
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    s.push(7)
    s.push(9)
    print(s.top())
    s.push(4)
    print(s.len())
    print(s.pop())
    s.push(6)
    print(s._data)

if __name__ == "__main__":
    usage()
