'''
7.8 Describe a nonrecursive method for finding, by link hopping, the middle
node of a doubly linked list with header and trailer sentinels. In the case
of an even number of nodes, report the node slightly left of center as the
“middle.” (Note: This method must only use link hopping; it cannot use a
counter.) What is the running time of this method?
'''

from DoublyLinkedListBase import _DoublyLinkedListBase, printDoublyLinkedList

if __name__ == "__main__":
    l = _DoublyLinkedListBase()
    for i in range(6):
        l.add_last(i+1)
    printDoublyLinkedList(l)

    start = l.first()
    end = l.last()
    while True:
        if start == end or (start.next == end and end.prev == start):
            break
        start = start.next
        end = end.prev
    
    print(start.element)