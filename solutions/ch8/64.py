'''
8.64 Implement the binary tree ADT using the array-based representation described
in Section 8.3.2.
'''
from ArrayBinaryTreeFactory import ArrayBinaryTreeFactory


if __name__ == "__main__":
    tree = ArrayBinaryTreeFactory.create('( 1 ( 2 ( 4 (5) (6) ) ) (3) )')
    #print(tree._data)
    #tree.delete(tree.find(2))
    #print(tree._data)
    #tree.delete_subtree(tree.find(2))
    #print(tree._data)

    subtree = tree.subtree(tree.find(2))
    print(subtree._data)