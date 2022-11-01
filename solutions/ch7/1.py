'''
7.1 Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
'''
from LinkedList import LinkedList

if __name__ == "__main__":
    l = LinkedList()
    for i in range(2):
        l.add_last(i)

    # find second-to-last node
    if len(l) <= 1:
        print('List must be at least of length 2')
        quit()

    n = l.first()
    while n._next._next != None:
        n = n._next
    print(n._element)