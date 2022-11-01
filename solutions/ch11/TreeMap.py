
from solutions.ch8.LinkedBinaryTree import LinkedBinaryTree
from solutions.ch10.Map import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    
    # -------------------------- override Position class --------------------------

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key()
        
        def value(self):
            return self.element()._value()

    #------------------------------- nonpublic utilities -------------------------------

    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():
            return p
        elif k < p.key():
            if p.left() != None:
                return self._subtree_search(p.left(), k)
        else:
            if p.right() != None:
                return self._subtree_search(p.right(), k)
        
        return p

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while walk.left() != None:
            walk = walk.left()
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while walk.right() != None:
            walk = walk.right()
        return walk
    
    #--------------------- public methods providing "positional" support ---------------------

    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order."""
        self._validate(p)
        if p.left() != None:
            return self._subtree_last_position(p)
        else:
            walk = p
            while self.parent(walk) != None and self.parent(walk).right() != walk:
                walk = self.parent(walk)

        return self.parent(walk)

    def after(self, p):
        """Return the Position just after p in the natural order."""
        self._validate(p)
        if p.right() != None:
            return self._subtree_first_position(p)
        else:
            walk = p
            while self.parent(walk) != None and self.parent(walk).left() != walk:
                    walk = self.parent(walk)

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        
        p = self._subtree_search(self.root(), k)
        return p

    #--------------------- public methods for (standard) map interface ---------------------    

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""  
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        
        p = self._subtree_search(self.root(), k)
        if p.key() == k:
            return p.value()
        else:
            raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""        
        if self.is_empty():
            self.add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                p.element()._value = v
            elif k < p.key():
                self.add_left(p, self._Item(k, v))
            else:
                self.add_right(p, self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self._delete(p)
                return

            raise KeyError('Key Error: ' + repr(k))

    def __iter__(self):
        return self.inorder()

    #--------------------- private methods ---------------------   

    def _delete(self, p):
        self._validate(p)
        if self.num_children(p) < 2:
            self.delete(p)
        else:
            q = self._subtree_last_position(p.left())
            self.replace(p, q)
            self._delete(q)