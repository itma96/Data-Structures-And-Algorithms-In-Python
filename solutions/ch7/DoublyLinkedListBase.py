from solutions.ch7.Empty import Empty

from re import L
from copy import deepcopy

class _DoublyLinkedListBase:
    class _Node:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev=None, next=None) -> None:
            self.element = element
            self.prev = prev
            self.next = next
    
    def __init__(self) -> None:
        self._header = self._Node(None)
        self._trailer = self._Node(None)
        self._header.next, self._trailer.prev = self._trailer, self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._header.next

    def last(self):
        return self._trailer.prev

    def _insert_between(self, n, predecessor, successor):
        n.prev, n.next = predecessor, successor
        predecessor.next = successor.prev = n
        self._size += 1
        return n
    
    def _delete_node(self, n):
        predecessor, successor = n.prev, n.next
        predecessor.next, successor.prev = successor, predecessor
        e = n.element
        n.prev = n.next = n.element = None
        self._size -= 1
        return e

    def add_first(self, e):
        newest = self._Node(e)
        self._insert_between(newest, self._header, self._header.next)
    
    def add_last(self, e):
        newest = self._Node(e)
        self._insert_between(newest, self._trailer.prev, self._trailer)

    def delete_first(self):
        e = self._delete_node(self._header.next)
        return e

    def delete_last(self):
        e = self._delete_node(self._trailer.prev)
        return e

    '''
    7.33 Modify the DoublyLinkedBase class to include a reverse method that reverses
    the order of the list, yet without creating or destroying any nodes.    
    '''
    def reverse(self):
        if len(self) == 1:
            return
        
        first = self.first()
        last = self.last()

        # update next links
        curr, next = first, first.next
        while next != self._trailer:
            next.next, curr, next = curr, next, next.next

        # update prev links
        curr, prev = last, last.prev
        while prev != self._header:
            prev.prev, prev, curr = curr, prev.prev, prev

        # update boundries
        self._header.next, self._trailer.prev = last, first
        first.next, last.prev = self._trailer, self._header

    def sublist(self, end, start=0):
        if start < 0 or end > len(self) or end < start:
            raise ValueError('Invalid sublist range')
        
        sublist = type(self)()
        
        curr = self._header.next
        for _ in range(start):
            curr = curr.next

        for _ in range(end - start):
            sublist.add_last(deepcopy(curr.element))
            curr = curr.next

        return sublist




def printDoublyLinkedList(dll):
    if dll._size == 0:
        print('[header]<->[trailer]')
        return

    s = '[header]<->'

    curr = dll.first()
    while curr != dll._trailer:
        s += '{}<->'.format(curr.element)
        curr = curr.next
    
    s += '[trailer]'

    print(s)

def usage():
    dll = _DoublyLinkedListBase()
    print(len(dll))
    print(dll.is_empty())
    dll.add_first(1)
    dll.add_last(2)
    dll.add_first(3)
    printDoublyLinkedList(dll)
    #print(dll.delete_last())
    #print(dll.delete_first())
    #printDoublyLinkedList(dll)
    #print(dll.delete_last())
    #printDoublyLinkedList(dll)
    dll.reverse()
    printDoublyLinkedList(dll)    


if __name__ == "__main__":
    usage()