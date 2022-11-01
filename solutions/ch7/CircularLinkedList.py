from solutions.ch7.Empty import Empty

class CircularLinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None) -> None:
            self._element = element
            self._next = next 

        def __str__(self) -> str:
            return '<_Node: _element={}, _next={}>'.format(self._element, self.next)

    def __init__(self) -> None:
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self._tail._next

    def last(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self._tail

    def add_last(self, e):
        n = self._Node(e)      
        if self.is_empty():
            n._next = n
            self._tail = n
        else:
            n._next, self._tail._next = self._tail._next, n
            self._tail = n
        self._size += 1
        return n

    def delete_last(self):
        if self.is_empty():
            raise Exception('List is empty')
        
        old_value = self._tail._element
        if self._size == 1:
            self._tail = None
        else:
            n = self._tail._next
            while n._next != self._tail:
                n = n._next
            
            n._next = self._tail._next
            self._tail = n
        self._size -= 1
        return old_value

    def delete_first(self):
        if self.is_empty():
            raise Exception('List is empty')
        old_value = self.first()._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = self.first()._next
        self._size -=1
        return old_value

def printCircularList(l):
    if l._size == 0:
        raise Empty("List is empty")

    head = l._tail._next
    s = '{}'.format(head._element)
    while head._next != l._tail._next:
        s += '->{}'.format(head._next._element)
        head = head._next
    s += '->{}->...'.format(head._next._element)
    print(s)        

def usage():
    L = CircularLinkedList()

    L.add_last(1)
    L.add_last(2)
    L.add_last(3)
    printCircularList(L)
    print(L.delete_first())   
    printCircularList(L)        
    print(L.delete_last())
    printCircularList(L) 

if __name__ == "__main__":
    usage()
