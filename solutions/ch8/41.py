'''
8.41 Describe how to clone a LinkedBinaryTree instance representing a proper
binary tree, with use of the attach method.
'''
from LinkedTreeFactory import LinkedTreeFactory
from Traversals import parenthesize

if __name__ == "__main__":
    tree = LinkedTreeFactory.create("( 1 ( 3 (6)) ( 2 (4) ( 5 (8) (7) ) ) )")
    clone = tree.clone()
    parenthesize(tree)
    print('\n')
    parenthesize(clone)
    tree.replace(tree.root(), 5)
    print('\n')
    parenthesize(tree)
    print('\n')
    parenthesize(clone)