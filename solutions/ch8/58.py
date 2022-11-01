'''
8.58 Let T be a tree with n positions. Define the lowest common ancestor
(LCA) between two positions p and q as the lowest position in T that has
both p and q as descendants (where we allow a position to be a descendant
of itself ). Given two positions p and q, describe an efficient algorithm for
finding the LCA of p and q. What is the running time of your algorithm?

eg.                 1
                  / | \
                 2  3  6
                / \   /|\
               4   5 8 9 10
                  /    |
                 7     11
'''
from LinkedTreeFactory import LinkedTreeFactory
from math import ceil, log

def LCA1(T, p, q):
    p_path = [p]
    q_path = [q]

    while not T.is_root(p):
        p = T.parent(p)
        p_path.append(p)

    while not T.is_root(q):
        q = T.parent(q)
        q_path.append(q)

    for i in p_path:
        if i in q_path:
            return i

    return T.root()

#----------------------------------------------------#

def LCA2(T, p, q):
    result = []
    findLCA(T, T.root(), p, q, result)
    return result[0] if result else None

def findLCA(T, candidate, p, q, result):

    found = False
    if candidate == p or candidate == q:
        found = True
    
    count = 0
    for child in T.children(candidate):
        if findLCA(T, child, p, q, result):
            count += 1

    if (found and count == 1) or count == 2:
        if len(result) == 0:
            result.append(candidate)
        return True
    else:
        return found or count == 1

#----------------------------------------------------#
# taken from: https://www.geeksforgeeks.org/lca-for-general-or-n-ary-trees-sparse-matrix-dp-approach-onlogn-ologn/

def dfs(T, p, depths, curr_depth=0):
    depths[p] = curr_depth    
    
    if T.is_leaf(p):
        return
    
    for child in T.children(p):
        dfs(T, child, depths, curr_depth + 1)


def memoize(func):
    kwargs = {'nodes': None, 'depths': None, 'parents': None}       
    def wrapper(*args):
        result, kwargs['nodes'], kwargs['depths'], kwargs['parents'] = func(*args, **kwargs)
        return result
    return wrapper

@memoize
def LCA3(T, p, q, **kwargs):

    nodes = kwargs['nodes']
    depths = kwargs['depths']
    parents = kwargs['parents']

    N = len(T)
    MAX_LEVEL = ceil(log(N))
    
    if nodes == None:
        nodes = list(T.preorder())

    if depths == None:
        # 0. pre-compute the depth for each node
        # time complexity : O(n)
        depths = dict.fromkeys(nodes, 0)
        dfs(T, T.root(), depths)     

    if parents == None:
        # 0. pre-compute for each node the 2^ith parent (0 <= i < MAX_LEVEL)
        # time complexity : O(n)        
        parents = [dict.fromkeys(nodes, -1) for _ in range(MAX_LEVEL)]

        for node in nodes:
            if T.parent(node) != None:
                parents[0][node] = T.parent(node)

        for i in range(1, MAX_LEVEL):
            for node in nodes:
                if parents[i-1][node] != -1:
                    parents[i][node] = parents[i-1][parents[i-1][node]]

    # 1. bring both nodes to same height

    if depths[q] < depths[p]:
        p, q = q, p

    diff = depths[q] - depths[p]

    for i in range(MAX_LEVEL):
        if (diff >> i) & 1:
            q = parents[i][q]

    # 2. parent-hop both nodes at the same time until they meet
    if (p == q):
        return p, nodes, depths, parents

    for i in range(MAX_LEVEL-1, -1, -1):
        if parents[i][p] != parents[i][q]:
            p = parents[i][p]
            q = parents[i][q]

    return parents[0][p], nodes, depths, parents


    
if __name__ == "__main__":
    tree = LinkedTreeFactory.create("( 1 ( 2 (4) ( 5 (7) ) ) (3) ( 6 (8) ( 9 (11) ) (10) ) )")
    p = tree.find(8)
    q = tree.find(11)
    lca = LCA3(tree, p, q)
    print(lca.element())

    p = tree.find(2)
    q = tree.find(7)
    lca = LCA3(tree, p, q)    
    print(lca.element())