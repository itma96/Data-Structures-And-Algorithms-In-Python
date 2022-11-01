'''
8.43 We can define a binary tree representation T' for an ordered general tree
T as follows (see Figure 8.23):
• For each position p of T, there is an associated position p' of T'.
• If p is a leaf of T, then p' in T' does not have a left child; otherwise
the left child of p' is q', where q is the first child of p in T.
• If p has a sibling q ordered immediately after it in T, then q' is the
right child of p' in T; otherwise p' does not have a right child.

eg.            1                      1
             / | \                   /
            2  3  6    ===>         2
           / \    |                / \
          4   5   7               4   3
                                   \   \
                                    5   6
                                       /
                                      7
'''

from LinkedBinaryTree import LinkedBinaryTree
from LinkedTreeFactory import LinkedTreeFactory
from Traversals import parenthesize

def binary_tree_representation(p):
    tree = p.container()
    parent = tree.parent(p)    
    bintree = LinkedBinaryTree(p.element()) 

    if not tree.is_leaf(p):
        first_child = tree.subtrees(p)[0]
        bintree.attach_left(binary_tree_representation(first_child.root()))

    if tree.parent(p) == None:
        return bintree

    index = parent._node._children.index(p._node)
    if index < len(parent._node._children) - 1:
        right_sibling = tree.subtree(tree._make_position(parent._node._children[index + 1]))
    else:
        right_sibling = None

    if right_sibling != None:
        bintree.attach_right(binary_tree_representation(right_sibling.root()))
    return bintree

if __name__ == "__main__":
    tree = LinkedTreeFactory.create("( 1 ( 2 (4) (5) ) (3) ( 6 (7) ) )")
    #tree = LinkedTreeFactory.create("( 1 (2) (3) (4) (5))")    
    bintree = binary_tree_representation(tree.clone().root())
    parenthesize(tree)
    print('\n')
    parenthesize(bintree)