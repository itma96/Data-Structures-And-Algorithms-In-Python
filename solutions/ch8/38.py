'''
8.38 Add support in LinkedBinaryTree for a method, delete subtree(p), that
removes the entire subtree rooted at position p, making sure to maintain
the count on the size of the tree. What is the running time of your implementation?

e.g.         1              1
           /   \          /   \
          2     3        3     2
         / \   /          \   / \
        4   5 6            6 4   5
           / \                  / \
          7   8                8   7

'''
from LinkedTreeFactory import LinkedTreeFactory
from LinkedBinaryTreeFactory import LinkedBinaryTreeFactory
from Traversals import parenthesize

if __name__ == "__main__":
    tree = LinkedBinaryTreeFactory.create("( 1 ( 3 (6)) ( 2 (4) ( 5 (8) (7) ) ) )")
    p = tree.right(tree.root())
    subtree = tree.delete_subtree(p)
    parenthesize(tree)
    parenthesize(subtree)

    tree = LinkedTreeFactory.create("( 1 ( 3 (6)) ( 2 (4) ( 5 (8) (7) ) ) )")
    children = tree.children(tree.root())
    next(children)
    p = next(children)
    subtree = tree.delete_subtree(p)
    parenthesize(tree)
    parenthesize(subtree)