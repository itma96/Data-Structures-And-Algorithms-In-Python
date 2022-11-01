'''
7.39 To better model a FIFO queue in which entries may be deleted before
reaching the front, design a PositionalQueue class that supports the complete
queue ADT, yet with enqueue returning a position instance and support
for a new method, delete(p), that removes the element associated
with position p from the queue. You may use the adapter design pattern
(Section 6.1.2), using a PositionalList as your storage.
'''
from PositionalList import PositionalList
from DoublyLinkedListBase import printDoublyLinkedList

class PositionalQueue:
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def enqueue(self, e):
        return self._data.add_last(e)

    def dequeue(self):
        return self._data.delete_first()

    def delete(self, p):
        self._data.delete(p)

if __name__ == "__main__":
    q = PositionalQueue()
    q.enqueue(1)
    q.enqueue(2)
    x = q.enqueue(3)
    q.enqueue(4)
    q.delete(x)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.is_empty())