'''
7.9 Give a fast algorithm for concatenating two doubly linked lists L and M,
with header and trailer sentinel nodes, into a single list L'
'''
from DoublyLinkedListBase import _DoublyLinkedListBase, printDoublyLinkedList

def deepcopy(l):
    copy = _DoublyLinkedListBase()
    
    curr = l.first()
    while(curr != l._trailer):
        copy.add_last(curr.element)
        curr = curr.next

    return copy

def concat_lists(l1, l2):
    l1_copy = deepcopy(l1)
    l2_copy = deepcopy(l2)

    l1_copy.last().next = l2_copy.first()
    l2_copy.first().prev = l1_copy.last()
    
    l1_copy._trailer = l2_copy._trailer
    l1_copy._size = l1_copy._size + l2_copy._size

    return l1_copy

if __name__ == "__main__":
    l1, l2 = _DoublyLinkedListBase(), _DoublyLinkedListBase()
    for i in range(5):
        l1.add_last(i)
    for i in range(5, 10):
        l2.add_last(i)
    l = concat_lists(l1, l2)
    printDoublyLinkedList(l)

