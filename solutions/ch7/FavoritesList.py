from solutions.ch7.PositionalList import PositionalList

class FavoritesList:
    class _Item:
        __slots__ = 'value', 'count'

        def __init__(self, value, count):
            self.value = value
            self.count = count

        def __eq__(self, other):
            return (self.value == other.value and self.count == other.count)
        
        def __ne__(self, other):
            return not self == other

        def __str__(self):
            return '<Item: value={} count={}>>'.format(self.value, self.count)
    
    def __init__(self):
        self._list = PositionalList()

    def __len__(self):
        return len(self._list)
    
    def is_empty(self):
        return len(self._list) == 0

    def _find(self, item):
        p = self._list.find_position(item)
        if p is None:
            raise ValueError('item does not exist')
        else:
            return p

    def _move_up(self, p):
        if p == self._list.first():
            return p
        value = p.element().count
        marker = self._list.before(p)
        while marker != self._list.first() and marker.element().count < value:
            marker = self._list.before(marker)
        
        return self._list.add_before(marker,  self._list.delete(p))  # delete/reinsert

    def add_item(self, value, count=0):
        item = self._Item(value, count)
        p = self._list.add_last(item)
        p = self._move_up(p)
        return p.element()

    def access(self, item):
        p = self._find(item)
        p.element().count += 1
        p = self._move_up(p)
        return p.element()

    def remove(self, item):
        p = self._find(item)
        self._list.delete(p)
        return item

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        current = self._list.first()
        for i in range(k):
            item = current.element()
            yield item
            current = self._list.after(current)
    '''
    7.23 Implement a reset counts( ) method for the FavoritesList class that resets
    all elements' access counts to zero (while leaving the order of the list
    unchanged).
    '''
    def reset_counts(self):
        p = self._list.first()
        while p is not None:
            p.element().count = 0
            p = self._list.after(p)


def usage():
    list = FavoritesList()
    a = list.add_item("Bon Jovi - It's my life")
    b = list.add_item("Bonnie Taylor - Total eclipse of my heart")
    c = list.add_item("Modern Talking - Cheri Cheri Lady", 3)
    list.access(b)

    for i in list.top(2):
        print(i)

    list.reset_counts()

    for i in list.top(2):
        print(i)

if __name__ == "__main__":
    usage()
