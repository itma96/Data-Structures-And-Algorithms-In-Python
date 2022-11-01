'''
7.2 Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L'
that contains all the nodes of L followed by all the nodes of M.
'''
from LinkedList import LinkedList, printList


def concatenate(n1, n2):
    result = LinkedList()

    result.add_last(n1._element)
    while n1._next != None:
        n1 = n1._next
        result.add_last(n1._element)        

    result.add_last(n2._element)
    while n2._next != None:
        n2 = n2._next
        result.add_last(n2._element)

    return result

if __name__ == "__main__":
    L = LinkedList()
    M = LinkedList()

    for i in range(5):
        L.add_last(i)
    for i in range(5, 10):
        M.add_last(i)

    result = concatenate(L.first(), M.first())
    printList(result)