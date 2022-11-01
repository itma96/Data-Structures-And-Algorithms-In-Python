from solutions.ch7.Empty import Empty

class LinkedList:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next) -> None:
            self._element = element
            self._next = next
        
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self._size == 0:
            raise Empty("List is empty")

        return self._head

    def last(self):
        if self._size == 0:
            raise Empty("List is empty")

        return self._tail

    def add_first(self, e):
        newest = self._Node(e, self._head)
        self._head = newest
        if self.is_empty():
            self._tail = newest
        self._size += 1
    
    def add_last(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1

    def delete_first(self):
        if self._size == 0:
            raise Empty("List is empty")

        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        return value

    def delete_last(self):
        if self._size == 0:
            raise Empty("List is empty")

        value = self._tail._element

        if self._head == self._tail:
            self._head = self._tail = None
            self._size = 0
            return value

        curr = self._head
        while curr._next != self._tail:
            curr = curr._next

        curr._next = None
        self._tail = curr
        self._size -= 1
        
        return value


def printList(l):
    if l._size == 0:
        raise Empty("List is empty")

    head = l._head
    s = '{}'.format(head._element)
    while head._next != None:
        s += '->{}'.format(head._next._element)
        head = head._next
    print(s)

def usage():
    l = LinkedList()
    l.add_first(1)
    l.add_first(2)
    l.add_first(3)
    printList(l)
    l.add_last(4)
    l.add_last(5)
    printList(l)
    print(l.delete_first())
    printList(l)
    print(l.delete_last())
    printList(l)
    print(len(l))
    print(l.delete_last())
    print(l.delete_last())
    printList(l)
    print(l.delete_last())
    print(l.is_empty())
    l.add_first(1)
    printList(l)
    l.add_first(2)
    l.add_first(3)
    printList(l)
    print(l.delete_first())
    print(l.delete_first())
    print(l.delete_first())
    print(l.is_empty())
    l.add_last(1)
    l.add_first(2)
    printList(l)

    
if __name__ == "__main__":
    usage()