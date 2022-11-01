'''
8.44 Give an efficient algorithm that computes and prints, for every position p
of a tree T, the element of p followed by the height of p’s subtree.
'''

from LinkedTreeFactory import LinkedTreeFactory


def postorder(T):
    root = T.root()
    heights = []
    for child in T.subtrees(root):
        heights.append(postorder(child))

    if T.is_leaf(root):
        print('{}: {}'.format(root.element(), 1))
        return 2
    else:
        print('{}: {}'.format(root.element(), max(heights)))
        return 1 + max(heights)

if __name__ == "__main__":
    tree = LinkedTreeFactory.create("( 1 ( 2 (4) (5) ) (3) ( 6 (7) ) )")
    postorder(tree)