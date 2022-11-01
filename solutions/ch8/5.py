'''
8.5 Describe an algorithm, relying only on the BinaryTree operations, that
counts the number of leaves in a binary tree that are the left child of their
respective parent.
'''
from Traversals import parenthesize
from LinkedBinaryTreeFactory import LinkedBinaryTreeFactory


if __name__ == "__main__":
    tree = LinkedBinaryTreeFactory.create("(1 (2 (3 (4)) (5)) ())")
    

