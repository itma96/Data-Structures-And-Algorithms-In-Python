'''
7.3 Describe a method for performing a card shuffle of a list of 2n elements,
by converting it into two lists. A card shuffle is a permutation where a list
L is cut into two lists, L1 and L2, where L1 is the first half of L and L2 is the
second half of L, and then these two lists are merged into one by taking
the first element in L1, then the first element in L2, followed by the second
element in L1, the second element in L2, and so on.
'''
from PositionalList import PositionalList

def shuffle(l1, l2):
    if len(l1) != len(l2):
        raise ValueError('Sublists must be of equal size')
    result = PositionalList()

    p, q = l1.first(), l2.first()
    for _ in range(len(l1)):
        result.add_last(p.element())
        result.add_last(q.element())
        p = l1.after(p)
        q = l2.after(q)
    return result


if __name__ == "__main__":
    l = PositionalList()
    for i in range(10):
        l.add_last(i)

    l1 = l.sublist(5, 0)
    l2 = l.sublist(10, 5)

    res = shuffle(l1, l2)

    print('-----------')
    for e in res:
        print(e)
    print('-----------')

    