'''
8.65 Implement the tree ADT using a linked structure as described in Section
8.3.3. Provide a reasonable set of update methods for your tree.
'''
from LinkedTreeFactory import LinkedTreeFactory
from Traversals import parenthesize

if __name__ == "__main__":
    tree = LinkedTreeFactory.create('( 1 ( 2 ( 4 (5) (6) ) ) (3) )')
    #parenthesize(tree)
    #tree.delete(tree.find(2))
    #parenthesize(tree)
    #tree.delete_subtree(tree.find(2))
    #parenthesize(tree)

    subtree = tree.subtree(tree.find(2))
    parenthesize(subtree)