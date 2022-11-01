'''
7.37 Implement a function that accepts a PositionalList L of n integers sorted
in nondecreasing order, and another value V, and determines in O(n) time
if there are two elements of L that sum precisely toV. The function should
return a pair of positions of such elements, if found, or None otherwise.
'''
from PositionalList import PositionalList, insertion_sort
import random

def two_sum(list, value):
    if len(list) < 2:
        return None
    head = list.first()
    tail = list.last()
    while head != None and tail != None:
        if head.element() > value:
            return None
        if tail.element() > value:
            tail = list.before(tail)
            continue
        
        sum = head.element() + tail.element()
        if sum == value:
            return (head, tail)
        elif sum < value:
            head = list.after(head)
        else:
            tail = list.before(tail)

'''
def two_sum(list, value):
    d = {}
    p = list.first()
    while p is not None:
        if value - p.element() in d:
            return (d[value - p.element()], p)
        if p.element() not in d:
            d[p.element()] = p
        p = list.after(p)
    
    return None
'''

if __name__ == "__main__":
    L = PositionalList()
    for i in range(10):
        L.add_last(random.randint(0, 9))

    insertion_sort(L)

    print('-----------')
    for e in L:
        print(e)
    print('-----------')
    
    value = 7
    pair = two_sum(L, value)
    if pair:
        print('{} + {} = {}'.format(pair[0].element(), pair[1].element(), value))
    else:
        print('No pair found')