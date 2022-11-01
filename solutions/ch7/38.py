'''
7.38 There is a simple, but inefficient, algorithm, called bubble-sort, for sorting
a list L of n comparable elements. This algorithm scans the list n−1 times,
where, in each scan, the algorithm compares the current element with the
next one and swaps them if they are out of order. Implement a bubble sort
function that takes a positional list L as a parameter. What is the running
time of this algorithm, assuming the positional list is implemented with a
doubly linked list?
'''
from LinkedList import LinkedList, printList
import random

def bubble_sort(list):
    for _ in range(len(list)):
        prev, curr, next = None, list._head, list._head._next
        while next != None:
            if curr._element > next._element:
                # swap the two nodes
                curr._next, next._next = next._next, curr
                if prev:
                    prev._next = next
                else:
                    list._head = next
                prev, next = next, curr._next
            else:
                prev, curr, next = curr, next, next._next

        printList(list)

if __name__ == "__main__":
    L = LinkedList()
    for i in range(10):
        L.add_last(random.randint(0, 9))

    printList(L)

    bubble_sort(L)

    printList(L)
            
