from solutions.ch14.Graph import Graph
from solutions.ch6.ArrayQueue import ArrayQueue

from collections import OrderedDict

def dfs(g, u, discovered):
    """
    Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    discovered is an ordered dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be ”discovered” prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.

    Returns last discovered vertex
    """   
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            dfs(g, v, discovered)
    return list(discovered.keys())[-1]

def bfs(g, u, discovered):
    """
    Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.

    Returns last discovered vertex
    """
    q = ArrayQueue()
    q.enqueue(u)

    while not q.is_empty():
        u = q.dequeue()
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                q.enqueue(v)
    return list(discovered.keys())[-1]


def construct_path(u, discovered):
    path = [u]
    while discovered[u] != None:
        path.append(discovered[u].opposite(u))
        u = discovered[u].opposite(u)
    return path

if __name__ == "__main__":
    g = Graph()
    a = g.insert_vertex("A")
    b = g.insert_vertex("B")
    c = g.insert_vertex("C")
    d = g.insert_vertex("D")
    e = g.insert_vertex("E")
    f = g.insert_vertex("F")

    g.insert_edge(a, b)
    g.insert_edge(b, c)
    g.insert_edge(b, d)
    g.insert_edge(b, e)
    g.insert_edge(d, a)
    g.insert_edge(e, f)
    g.insert_edge(f, c)

    discovered = OrderedDict([(a, None)])
    last = dfs(g, a, discovered)
    print(last)
    print(construct_path(e, discovered))

    discovered = OrderedDict([(a, None)])
    last = bfs(g, a, discovered)
    print(last)
    print(construct_path(e, discovered))