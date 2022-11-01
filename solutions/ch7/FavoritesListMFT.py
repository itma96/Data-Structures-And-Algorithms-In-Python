from solutions.ch7.FavoritesList import FavoritesList
from solutions.ch7.PositionalList import PositionalList
from solutions.ch7.DoublyLinkedListBase import printDoublyLinkedList

class FavoritesListMFT(FavoritesList):

    def _move_up(self, p):
        if p != self._list.first():
            return self._list.add_first(self.remove(p.element()))
        else:
            return p

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        temp = PositionalList()
        for p in self._list:
            temp.add_last(p)

        for i in range(k):
            max = temp.first()
            curr = temp.after(max)
            while curr is not None:
                if curr.element().count > max.element().count:
                    max = curr
                curr = temp.after(curr)
            yield max.element()
            temp.delete(max)

def usage():
    list = FavoritesListMFT()
    a = list.add_item("Bon Jovi - It's my life", 2)
    b = list.add_item("Bonnie Taylor - Total eclipse of my heart")
    c = list.add_item("Modern Talking - Cheri Cheri Lady", 3)
    list.access(a)
    list.access(b)

    for i in list._list:
        print(i)

    print('---------')

    for i in list.top(3):
        print(i)

if __name__ == "__main__":
    usage()
