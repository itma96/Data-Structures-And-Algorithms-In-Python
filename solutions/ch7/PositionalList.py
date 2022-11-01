from solutions.ch7.DoublyLinkedListBase import _DoublyLinkedListBase

import builtins

class PositionalList(_DoublyLinkedListBase):
    
    class Position:
        __slots__ = 'container', 'node'

        def __init__(self, container, node):
            self.container = container
            self.node = node
        
        def element(self):
            return self.node.element
        
        def __eq__(self, other):
            return type(other) == type(self) and other.node == self.node
        
        def __ne__(self, other):
            return not (other == self)

        def __str__(self):
            return '<Position: container={}, node=<Node: element={}, prev={}, next={}>>'.format(self.container, self.node.element, self.node.prev, self.node.next)
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node == self._header or p.node == self._trailer:
            raise ValueError('p out of bounds')
        if p.node.prev is None and p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node
    
    def _make_position(self, n):
        if n is self._header or n is self._trailer:
            return None  # boundry violation
        return self.Position(self, n)
    
    def first(self):
        return self._make_position(super().first())

    def last(self):
        return self._make_position(super().last())

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        curr = self.first()
        while curr is not None:
            yield curr.element()
            curr = self.after(curr)

    '''
    7.15 Provide support for a reversed method of the PositionalList class that
    is similar to the given iter , but that iterates the elements in reversed
    order.
    '''
    def __reversed__(self):
        curr = self.last()
        while curr is not None:
            yield curr.element()
            curr = self.before(curr)
    
    def _insert_between(self, n, predecessor, successor):
        node = super()._insert_between(n, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        newest = self._Node(e)
        return self._insert_between(newest, self._header, self._header.next)

    def add_last(self, e):
        newest = self._Node(e)
        return self._insert_between(newest, self._trailer.prev, self._trailer)

    def add_before(self, p, e):
        newest = self._Node(e)
        node = self._validate(p)
        return self._insert_between(newest, node.prev, node)

    def add_after(self, p, e):
        newest = self._Node(e)
        node = self._validate(p)
        return self._insert_between(newest, node, node.next)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        old_val = node.element
        node.element = e
        return old_val

    '''
    7.13 Update the PositionalList class to support an additional method find(e),
    which returns the position of the (first occurrence of ) element e in the list
    (or None if not found).
    '''
    def find_position(self, e):
        current = self.first()
        while(current != None):
            if current.node.element == e:
                return current
            current = self.after(current)
        return current

    '''
    7.12 Redo the previously problem with max as a method of the PositionalList
    class, so that calling syntax L.max( ) is supported.
    '''
    def max(self):
        max = self.first().element()
        walk = self.after(self.first())
        while walk != self.last():
            if walk.element() > max:
                max = walk.element()
            walk = self.after(walk)
        return  builtins.max(max, self.last().element())

    '''
    7.34 Modify the PositionalList class to support a method swap(p, q) that causes
    the underlying nodes referenced by positions p and q to be exchanged for
    each other. Relink the existing nodes; do not create any new nodes.
    '''
    def swap(self, p, q):
        p = self._validate(p)
        q = self._validate(q)

        p_prev, p_next = p.prev, p.next
        q_prev, q_next = q.prev, q.next

        if p.next == q and q.prev == p:
            p_prev.next, p.next, q.next = q, q_next, p
            p.prev, q.prev, q_next.prev = q, p_prev, p
        else:
            p_prev.next, p.next, p_next.next, q.next = q, q_next, p, p_next
            q_next.prev, q.prev, q_prev.prev, p.prev = p, p_prev, q, q_prev
    
def usage():
    l = PositionalList()
    l.add_last(8)
    p = l.first()
    print(p)
    q = l.add_after(p, 5)
    print(q)
    print(l.before(q))
    r = l.add_before(q, 3)
    print(r.element())
    print(l.after(p))
    print(l.before(p))
    s = l.add_first(9)
    print(l.delete(l.last()))
    l.replace(p, 7)

    print('-----------')
    for e in l:
        print(e)
    print('-----------')

    print('-----------')
    for e in l.__reversed__():
        print(e)
    print('-----------')

    l.swap(l.first(), l.last())
    print('-----------')
    for e in l:
        print(e)
    print('-----------')

    l.swap(l.first(), l.after(l.first()))
    print('-----------')
    for e in l:
        print(e)
    print('-----------')    

    #printDoublyLinkedList(l._header)

def insertion_sort(l):
    if len(l) <= 1:
        return l
    marker = l.first()
    while marker != l.last():
        pivot = l.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != l.first() and l.before(walk).element() > value:
                walk = l.before(walk)
            l.delete(pivot)
            l.add_before(walk, value)
        
if __name__ == "__main__":
    usage()
    quit()
    l = PositionalList()
    l.add_first(9)
    l.add_last(7)
    l.add_last(1)
    l.add_last(5)

    print('-----------')
    for e in l:
        print(e)
    print('-----------')    
    
    insertion_sort(l)

    print('-----------')
    for e in l:
        print(e)
    print('-----------')    

