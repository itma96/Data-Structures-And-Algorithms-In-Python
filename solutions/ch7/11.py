'''
7.11 Implement a function, with calling syntax max(L), that returns the maximum
element from a PositionalList instance L containing comparable
elements.
'''
from PositionalList import PositionalList, printDoublyLinkedList
import random

def max(l):
    if len(l) == 1:
        return l.first().element()
    else:
        max = l.first().element()
        for element in l:
            if element > max:
                max = element
        return max

if __name__ == "__main__":
    L = PositionalList()
    for i in range(10):
        L.add_last(random.randint(0, 9))
    
    print(max(L))
    print(L.max())