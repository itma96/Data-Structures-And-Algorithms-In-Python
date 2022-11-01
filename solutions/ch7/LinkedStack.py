from solutions.ch7.Empty import Empty
from solutions.ch7.LinkedList import LinkedList

class LinkedStack:
    def __init__(self) -> None:
        self._data = LinkedList()

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return self._data.is_empty()

    def push(self, e):
        self._data.add_first(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack if empty")

        return self._data.first()._element

    def pop(self):
        if self.is_empty():
            raise Empty("Stack if empty")

        return self._data.delete_first()

def usage():
    s = LinkedStack()
    print(len(s))
    print(s.is_empty())
    s.push(1)
    print(s.top())
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.is_empty())

if __name__ == "__main__":
    usage()