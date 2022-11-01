'''
7.5 Implement a function that counts the number of nodes in a circularly
linked list.
'''
from CircularLinkedList import CircularLinkedList

def count(node):
    if node == count.tail:
        return 1
    else:
        return 1 + count(node._next)

if __name__ == "__main__":
    L = CircularLinkedList()
    for i in range(10):
        L.add_last(i)
    
    count.tail = L.last()
    print(count(L.first()))

