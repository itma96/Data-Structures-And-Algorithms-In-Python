'''
7.3 Describe a recursive algorithm that counts the number of nodes in a singly
linked list.
'''

from LinkedList import LinkedList

def count(n):
    if n == None:
        return 0
    else:
        return 1 + count(n._next)

if __name__ == "__main__":
    L = LinkedList()
    for i in range(10):
        L.add_last(i)
    
    count = count(L.first())
    print(count)