'''
8.35 Two ordered trees T' and T'' are said to be isomorphic if one of the following holds:
• Both T' and T'' are empty.
• The roots of T' and T'' have the same number k ≥ 0 of subtrees, and the i th such 
subtree of T' is isomorphic to the i th such subtree of T''
for i = 1, . . . , k

e.g.         1              1
           /   \          /   \
          2     3        3     2
         / \   /          \   / \
        4   5 6            6 4   5
           / \                  / \
          7   8                8   7

'''   
from LinkedBinaryTreeFactory import LinkedBinaryTreeFactory

def isomorphic(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    if tree1 == None or tree2 == None:
        return False
    subtrees1 = tree1.subtrees(tree1.root())
    subtrees2 = tree2.subtrees(tree2.root())
    return (isomorphic(subtrees1[0], subtrees2[0]) and isomorphic(subtrees1[1], subtrees2[1])) or \
        (isomorphic(subtrees1[0], subtrees2[1]) and isomorphic(subtrees1[1], subtrees2[0]))

if __name__ == "__main__":
    t1 = LinkedBinaryTreeFactory.create("( 1 ( 2 (4) ( 5 (7) (8) ) ) ( 3 (6) ) )")
    t2 = LinkedBinaryTreeFactory.create("( 1 ( 3 (6)) ( 2 (4) ( 5 (8) (7) ) ) )")
    print(isomorphic(t1, t2))