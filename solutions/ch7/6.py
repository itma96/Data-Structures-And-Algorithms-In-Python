'''
7.6 Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to the same list.
'''

from CircularLinkedList import CircularLinkedList


if __name__ == "__main__":
    L = CircularLinkedList()
    L.add_last(1)
    x = L.add_last(2)
    L.add_last(3)
    L.add_last(4)
    y = L.add_last(5)
    L.add_last(6)

    #z = L._Node(99)

    walk = x._next
    found = False
    while walk != x:
        if walk == y: #z
            found = True
            break
        walk = walk._next

    if found:
        print('Elements belong to the same list')
    else:
        print('Elements do not belong to the same list')