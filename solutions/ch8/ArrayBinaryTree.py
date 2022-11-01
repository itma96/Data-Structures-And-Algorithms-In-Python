#!/usr/bin/python
# -*- coding: utf-8 -*-
from BinaryTree import BinaryTree
from solutions.ch6.ArrayStack import ArrayStack


class ArrayBinaryTree(BinaryTree):

  # -------------------------- nested Position class --------------------------

    class Position(BinaryTree.Position):

        def __init__(self, container, index):
            self._container = container
            self._index = index

        def element(self):
            if 0 <= self._index < len(self._container):
                return self._container._data[self._index]
            else:
                return None

        def __eq__(self, other):
            return type(other) is type(self) and other._index \
                is self._index

        def __hash__(self):
            return hash((self._container, self._index))

  # ------------------------------- utility methods -------------------------------

    def _validate(self, p):
        """Return associated node, if position is valid."""

        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._index == -1:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        if p._index < 0 or p._index >= len(self._data):  # p is out of bounds
            return None
        return p._index

    def _make_position(self, i):
        """Return Position instance for given node (or None if no node)."""

        return (self.Position(self, i) if 0 <= i
                < len(self._data) else None)

    def _resize(self):
        index = len(self) - 1
        while index > 0 and self._data[index] == None:
            self._data.pop()
            index -= 1


  # -------------------------- constructors --------------------------

    def __init__(self, element=None):
        self._data = ([element] if element else [])

  # -------------------------- accessors --------------------------

    def __len__(self):
        return len(self._data)

    def root(self):
        return (self._make_position(0) if self._data else None)

    def parent(self, p):
        index = self._validate(p)
        return (self._make_position(index) if index else None)

    def left(self, p):
        index = self._validate(p)
        return (self._make_position(2 * index + 1) if index >= 0 else None)

    def right(self, p):
        index = self._validate(p)
        return (self._make_position(2 * index + 2) if index >= 0 else None)

    def num_children(self, p):
        index = self._validate(p)
        count = 0
        if self._data[2 * index + 1] != None:
            count += 1
        if self._data[2 * index + 2] != None:
            count += 1
        return count

    def siblings(self, p):
        index = self._validate(p)
        if index == 0:  # p is root
            return None
        if index / 2 == 0:  # p has left sibling
            return self.left(p)
        else:
            return self.right(p)  # p has right sibling

    def subtree(self, p):
        index = self._validate(p)

        subtree = ArrayBinaryTree(self._data[index])

        s = ArrayStack()
        s.push((subtree.root(), self.left(p), self.right(p)))

        while not s.is_empty():
            (q, left, right) = s.pop()
            if left != None and left.element() != None:
                r = subtree.add_left(q, left.element())
                s.push((r, self.left(left), self.right(left)))
            if right != None and right.element() != None:
                r = subtree.add_right(q, right.element())
                s.push((r, self.left(right), self.right(right)))        

        return subtree

  # -------------------------- mutators --------------------------

    def add_root(self, e):
        if self._data is not None:
            raise ValueError('Root exists')
        self._data.append(e)
        self._size = 1
        return self._make_position(0)

    def add_child(self, p, e):
        index = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Left and right children  already exist')
        (left_index, right_index) = (2 * index + 1, 2 * index + 2)
        if left_index < len(self):
            if self._data[left_index] == None:
                self._data[left_index] = e
                return self._make_position(left_index)
        elif right_index < len(self):
            if self._data[right_index] == None:
                self._data[right_index] == e
                return self._make_position(right_index)
        else:
            self._data.extend([None] * (left_index - len(self) + 1))
            self._data[left_index] == e
            return self._make_position(left_index)

    def add_left(self, p, e):
        index = self._validate(p)
        left_index = 2 * index + 1
        if left_index < len(self):
            if self._data[left_index] != None:
                raise ValueError('Left child already exists')
            else:
                self._data[left_index] = e
                return self._make_position(left_index)
        else:
            self._data.extend([None] * (left_index - len(self) + 1))
            self._data[left_index] = e
            return self._make_position(left_index)

    def add_right(self, p, e):
        index = self._validate(p)
        right_index = 2 * index + 2
        if right_index < len(self):
            if self._data[right_index] != None:
                raise ValueError('Right child already exists')
            else:
                self._data[right_index] = e
                return self._make_position(right_index)
        else:
            self._data.extend([None] * (right_index - len(self) + 1))
            self._data[right_index] = e
            return self._make_position(right_index)

    def find(self, e):
        for p in self.preorder():
            if p.element() == e:
                return p
        return None

    def replace(self, p, e):
        index = self._validate(p)
        old = self._data[index]
        self._data[index] = e
        return old

    def delete(self, p):
        index = self._validate(p)
        old = self._data[index]
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')

        (left, right) = (self.left(p), self.right(p))
        (left_index, right_index) = (left._index, right._index)

        if left_index < len(self) and left.element() != None:
            # shift up left subtree
            self._data[index] = self._data[left_index]
            while self.num_children(left) != 0:
                if self.left(left) != None:
                    self._data[left_index] = self.left(left).element()
                    self._data[2 * left_index + 1] = None
                if self.right(left) != None:
                    self._data[left_index + 1] = self.right(left).element()
                    self._data[2 * left_index + 2] = None

                left_index = 2 * left_index + 1
                
        elif right_index < len(self) and right.element() != None:
            # shift up right subtree
            self._data[index] = self._data[right_index]
            while self.num_children(right) != 0:
                if self.left(right) != None:
                    self._data[right_index] = self.left(right).element()
                    self._data[2 * right_index + 1] = None
                if self.right(right) != None:
                    self._data[right_index + 1] = self.right(right).element()
                    self._data[2 * right_index + 2] = None

                right_index = 2 * right_index + 1

        self._resize()

        return old
        

    def delete_subtree(self, p):
        if self._validate(p) == None:
            return

        if self.root() == p:
            raise ValueError('Position must be different than root')

        s = ArrayStack()
        s.push(p)

        while not s.is_empty():
            q = s.pop()

            if self.left(q) != None:
                s.push(self.left(q))
            if self.right(q) != None:
                s.push(self.right(q))

            self._data[q._index] = None  # delete q
            q._index = -1

        self._resize()

    def attach_left(self, t, p=None):
        if not type(self) is type(t):  # both trees must be same type
            raise TypeError('Tree types must match')

        if p == None:
            p = self.root()

        self._validate(p)

        # attach t's root node
        q = self.add_left(p, t.root().element())

        # attach t's other nodes

        s = ArrayStack()
        s.push((q, t.left(t.root()), t.right(t.root())))

        while not s.is_empty():
            (q, t_left, t_right) = s.pop()
            if t_left != None and t_left.element() != None:
                r = self.add_left(q, t_left.element())
                s.push((r, t.left(t_left), t.right(t_left)))
            if t_right != None and t_right.element() != None:
                r = self.add_right(q, t_right.element())
                s.push((r, t.left(t_right), t.right(t_right)))

    def attach_right(self, t, p=None):
        if not type(self) is type(t):  # both trees must be same type
            raise TypeError('Tree types must match')

        if p == None:
            p = self.root()

        self._validate(p)

        # attach t's root node
        q = self.add_right(p, t.root().element())

        # attach t's other nodes
        s = ArrayStack()
        s.push((q, t.left(t.root()), t.right(t.root())))

        while not s.is_empty():
            (q, t_left, t_right) = s.pop()
            if t_left != None and t_left.element() != None:
                r = self.add_left(q, t_left.element())
                s.push(r, t.left(t_left), t.right(t_left))
            if t_right != None and t_right.element() != None:
                r = self.add_right(q, t_right.element())
                s.push(r, t.left(t_right), t.rigth(t_right))


    def attach(self, t, p=None):
        if not type(self) is type(t):  # both trees must be same type
            raise TypeError('Tree types must match')

        if p == None:
            p = self.root()

        self._validate(p)

        if self.children(p) != 2:
            if self.left(p) == None:
                self.attach_left(t, p)
            else:
                self.attach_right(t, p)
        else:
            raise ValueError('Left and right children exist')