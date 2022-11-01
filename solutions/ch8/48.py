'''
8.48 Given a proper binary tree T, define the reflection of T to be the binary
tree T' such that each node v in T is also in T', but the left child of v in T
is v’s right child in T' and the right child of v in T is v’s left child in T'.
Show that a preorder traversal of a proper binary tree T is the same as the
postorder traversal of T’s reflection, but in reverse order.
'''

from LinkedBinaryTreeFactory import LinkedBinaryTreeFactory
from LinkedBinaryTree import LinkedBinaryTree
from Traversals import parenthesize

def reflection(T):
    root = T.root()
    result = LinkedBinaryTree(root.element())
    if T.is_leaf(root):
        return result
    else:
        left_subtree, right_subtree = T.subtrees(root)
        result.attach_left(reflection(right_subtree))
        result.attach_right(reflection(left_subtree))
        return result

if __name__ == "__main__":
    tree = LinkedBinaryTreeFactory.create("( 1 ( 2 (3) (4) ) (5 (6) (7)) )")
    reflected_tree = reflection(tree)
    parenthesize(tree)
    print('\n')
    parenthesize(reflected_tree)
