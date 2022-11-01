#!/usr/bin/python
# -*- coding: utf-8 -*-
from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):

    """Linked representation of a binary tree structure."""

    # -------------------------- nested _Node class --------------------------

    class _Node:

        """Lightweight, nonpublic class for storing a node."""

        __slots__ = ('_element', '_parent', '_left', '_right')  # streamline memory usage

        def __init__(
            self,
            element,
            parent=None,
            left=None,
            right=None,
            ):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    # -------------------------- nested Position class --------------------------

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node \
                is self._node

    # ------------------------------- utility methods -------------------------------

    def _validate(self, p):
        """Return associated node, if position is valid."""

        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""

        return (self.Position(self, node) if node is not None else None)

    # -------------------------- constructor --------------------------

    def __init__(self, element=None):
        """Create an initially empty binary tree."""

        self._root = self._Node(element) if element else None
        self._size = 1 if element else 0

    # -------------------------- accessors --------------------------

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def siblings(self, p):
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no siblings
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def subtree(self, p):
        node = self._validate(p)
        subtree = LinkedBinaryTree()
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
        if node._left is None:
            return self.add_left(p, e)
        elif node._right is None:
            return self.add_right(p, e)
        else:
            raise ValueError('Left and right children exist')

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)  # node is its parent
        return self._make_position(node._left)

    def add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)  # node is its parent
        return self._make_position(node._right)

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
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = (node._left if node._left else node._right)  # might be None
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def delete_subtree(self, p):
        node = self._validate(p)
        if self.root() == p:
            raise ValueError('Position must be different than root')
            
        if node == node._parent._left:  # if node is left child
            node._parent._left = None   # delete parent link
        else:                           # if node is right child
            node._parent._right = None  # delete parent link

        subtree = LinkedBinaryTree()
        node._parent = None
        subtree._root = node
        subtree._size = len(list(self._subtree_preorder(p)))
        self._size -= subtree._size  # update tree size
        return subtree

    def attach(self, t, p=None):
        if p == None:
            node = self._root
        else:
            node = self._validate(p)

        if node._left == None:
            self.attach_left(t, p)
        elif node._right == None:
            self.attach_right(t, p)
        else:
            raise ValueError('Left and right children exist')

    def attach_left(self, t, p=None):
        if not type(self) is type(t):  # both trees must be same type
            raise TypeError('Tree types must match')

        if p == None:
            node = self._root
        else:
            node = self._validate(p)
            if node._right != None:
                raise ValueError('Left child exits')

        self._size += len(t)
        if not t.is_empty():  # attached t as left subtree of node
            t._root._parent = node
            node._left = t._root
            t._root = None  # set t instance to empty
            t._size = 0

    def attach_right(self, t, p=None):
        if not type(self) is type(t):  # both trees must be same type
            raise TypeError('Tree types must match')

        if p == None:
            node = self._root
        else:
            node = self._validate(p)
            if node._right != None:
                raise ValueError('Right child exits')

        self._size += len(t)
        if not t.is_empty():  # attached t as right subtree of node
            t._root._parent = node
            node._right = t._root
            t._root = None  # set t instance to empty
            t._size = 0
