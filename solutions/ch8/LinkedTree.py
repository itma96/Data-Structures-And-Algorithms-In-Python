#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tree import Tree


class LinkedTree(Tree):

    """Linked representation of a binary tree structure."""

    # -------------------------- nested _Node class --------------------------

    class _Node:

        """Lightweight, nonpublic class for storing a node."""

        __slots__ = ('_element', '_parent', '_children')  # streamline memory usage

        # def __init__(self, element, parent=None, children=[]):

        def __init__(
            self,
            element,
            parent=None,
            children=None,
            ):
            self._element = element
            self._parent = parent
            self._children = (children if children else [])

        def __eq__(self, other):
            return type(other) is type(self) and other._element \
                is self._element and self._parent is other._parent \
                and self._children == other._children

        def __hash__(self):
            return hash((self._element, self._parent))

    # -------------------------- nested Position class --------------------------

    class Position(Tree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def container(self):
            return self._container

        def __eq__(self, other):
            return type(other) is type(self) and other._node \
                is self._node

        def __hash__(self):
            return hash((self._container, self._node))

    # ------------------------------- utility methods -------------------------------

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return (self.Position(self, node) if node is not None else None)

    # -------------------------- constructors --------------------------

    def __init__(self, element=None):
        self._root = (self._Node(element) if element else None)
        self._size = (1 if element else 0)

    # -------------------------- accessors --------------------------

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def children(self, p):
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def num_children(self, p):
        node = self._validate(p)
        return len(node._children)

    def siblings(self, p):
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no siblings
        else:
            for sibling in parent.element()._children:
                if p.element() != sibling:
                    yield self._make_position(sibling)

    def subtree(self, p):
        node = self._validate(p)
        subtree = LinkedTree()
        subtree._root = node
        subtree._size = len(list(self._subtree_preorder(p)))
        return subtree

    # -------------------------- mutators --------------------------

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_child(self, p, e):
        node = self._validate(p)
        child = self._Node(e, node)
        node._children.append(child)
        self._size += 1
        return self._make_position(child)

    def find(self, e):
        for p in self.preorder():
            if p.element() == e:
                return p
        return None

    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) >= 2:
            raise ValueError('Position has two or more children')
        child = node._children[0]
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            parent._children = [(child if x == node else x) for x in
                                parent._children]
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def delete_subtree(self, p):
        node = self._validate(p)
        if self.root() == p:
            raise ValueError('Position must be different than root')

        node._parent._children.remove(node)
        subtree = LinkedTree()
        node._parent = None
        subtree._root = node
        subtree._size = len(list(self._subtree_preorder(p)))
        self._size -= subtree._size  # update tree size
        return subtree

    def attach(self, t, p=None):
        if not type(self) is type(t):  # trees must be same type
            raise TypeError('Tree types must match')

        if p == None:
            node = self._root
        else:
            node = self._validate(p)
            if not self.is_leaf(p):
                raise ValueError('position must be leaf')

        self._size += len(t)
        if not t.is_empty():  # attached t as subtree of node
            node._children.append(t._root)  # dc insereaza si in t._root._children?!
            t._root._parent = node
            t._root = None  # set t instance to empty
            t._size = 0

    def _clone(self, p):
        t = LinkedTree(p.element())
        if self.is_leaf(p):
            return t
        else:
            for child in self.children(p):
                t.attach(self._clone(child))
        return t

    def clone(self):
        return self._clone(self.root())
