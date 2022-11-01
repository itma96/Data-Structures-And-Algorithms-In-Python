'''
7.29 Describe in detail an algorithm for reversing a singly linked list L using
only a constant amount of additional space and not using any recursion.
'''

from LinkedList import LinkedList, printList

def reverse(l):
    if len(l) == 1:
        return l
    
    current = l.first()
    next = current._next
    current._next = None
    while current != None and next != None:
        next._next, current, next = current, next, next._next
        
    l._head, l._tail = l._tail, l._head
    return l

if __name__ == "__main__":
    l = LinkedList()
    l.add_last(1)
    l.add_last(2)
    l.add_last(3)
    l.add_last(4)

    l = reverse(l)
    printList(l)
    print(len(l))
    