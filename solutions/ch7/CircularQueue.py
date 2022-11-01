from solutions.ch7.CircularLinkedList import CircularLinkedList, printCircularList

class CircularQueue:
    def __init__(self) -> None:
        self._data = CircularLinkedList()

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return self._data.is_empty()

    def enqueue(self, e):
        self._data.add_last(e)
    
    def dequeue(self):
        return self._data.delete_first()

    def rotate(self):
        self._data._tail = self._data._tail._next

def usage():
    q = CircularQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    q.rotate()

    printCircularList(q._data)

if __name__ == "__main__":
    usage()