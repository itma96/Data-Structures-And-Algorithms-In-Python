#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tree import Tree


class BinaryTree(Tree):

    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------

    def left(self, p):
        """
        Return a Position representing p's left child.

        Return None if p does not have a left child.
        """

        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """
        Return a Position representing p's right child.

        Return None if p does not have a right child.
        """

        raise NotImplementedError('must be implemented by subclass')

    def add_left(self, p, e):
        """
        Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """

        raise NotImplementedError('must be implemented by subclass')

    def add_right(self, p, e):
        """
        Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """

        raise NotImplementedError('must be implemented by subclass')

    def attach_left(self, t, p=None):
        """
        Attach trees t as the left subtree of the external Position p.

        As a side effect, set t to empty.
        Raise TypeError if tree t does not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """

        raise NotImplementedError('must be implemented by subclass')

    def attach_right(self, t, p=None):
        """
        Attach trees t as the right subtree of the external Position p.

        As a side effect, set t to empty.
        Raise TypeError if tree t does not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """

        raise NotImplementedError('must be implemented by subclass')

    def subtree(self, p):
        """Return a subtree of the current tree, rooted at Position."""

        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""

        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def subtrees(self, p):
        """Returns a list of subtrees of a given Position, if any."""

        self._validate(p)
        result = [None, None]
        if self.left(p) is not None:
            result[0] = self.subtree(self.left(p))
        if self.right(p) is not None:
            result[1] = self.subtree(self.right(p))

        return result

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""

        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""

        if self.left(p) is not None:  # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p  # visit p between its subtrees
        if self.right(p) is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions."""

        return self.inorder()  # make inorder the default
