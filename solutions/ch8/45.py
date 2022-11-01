'''
8.45 Give an O(n)-time algorithm for computing the depths of all positions of
a tree T, where n is the number of nodes of T
'''

from LinkedTreeFactory import LinkedTreeFactory

def preorder(T, depth):
    yield (T.root().element(), depth + 1)

    for subtree in T.subtrees(T.root()):
        yield from preorder(subtree, depth + 1)

if __name__ == "__main__":
    tree = LinkedTreeFactory.create("( 1 ( 2 (4) (5) ) (3) ( 6 (7) ) )")
    print(sorted(preorder(tree, -1), key=lambda x: x[1]))