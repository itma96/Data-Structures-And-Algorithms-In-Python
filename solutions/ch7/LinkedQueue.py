from solutions.ch7.Empty import Empty
from solutions.ch7.LinkedList import LinkedList, printList

class LinkedQueue:
    
    def __init__(self) -> None:
        self._data = LinkedList()
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return self._data.is_empty()

    def enqueue(self, e):
        self._data.add_last(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        e = self._data.delete_first()
        return e

    def rotate(self):
        old_head = self._data.first()
        old_tail = self._data.last()

        self._data._head = old_head._next
        old_tail._next = old_head

        self._data._tail = old_head
        old_head._next = None

    '''
    7.26 Implement a method, concatenate(Q2) for the LinkedQueue class that
    takes all elements of LinkedQueue Q2 and appends them to the end of the
    original queue. The operation should run in O(1) time and should result
    in Q2 being an empty queue.
    '''
    def concatenate(self, q):
        self._data._tail._next = q._data._head
        self._data._tail = q._data._tail
        self._data._size += q._data._size

        q._data._head, q._data._tail = None, None
        q._data._size = 0

def usage():
    q = LinkedQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    q.rotate()
    q.rotate()
    q.rotate()
    printList(q._data)

    p = LinkedQueue()
    p.enqueue(4)
    p.enqueue(5)
    p.enqueue(6)

    q.concatenate(p)
    printList(q._data)
    print(len(p))
    print(p.is_empty())

    #printList(q._data)
    #print(q.dequeue())
    #print(q.dequeue())
    #print(q.dequeue())
    #print(q.is_empty())

if __name__ == "__main__":
    usage()