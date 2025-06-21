"""
Approach:
    Let us see how we can get the minimum cost to walk from node a to node b in a weighted graph. Let say we have 5 values, 
    to get the minimum AND value, we simply take the AND of all the values, given the fact that we can visit same edge multiple times.
    So if there is a path from a to b, we can get the minimum AND value by taking the AND of all the edges in that path.
    We can use a union-find data structure to group the nodes into connected components. For each component, we can calculate the AND of all edges
    in that component. Then, for each query, we can check if the two nodes belong to the same component and return the AND value of that component, else return -1.
Time Complexity:
    O(n + m + q) where n is the number of nodes, m is the number of edges, and q is the number of queries.
Space Complexity:
    O(n) for the union-find data structure
"""

def minimumCost(n: int, edges, query):

    p = list(range(n))

    size = [1] * n
    def find_parent(x):
        if p[x] != x:
            p[x] = find_parent(p[x])
        return p[x]

    def union(u,v):
        x,y = find_parent(u), find_parent(v)
        if x != y:
            if size[x] < size[y]:
                p[x] = y
                size[y] += size[x]
            else:
                p[y] = x
                size[x] += size[y]


    for u,v,w in edges:
        union(u,v)
    components = {}

    for u,v,w in edges:
        root = find_parent(u)
        if root not in components:
            components[root] = w
        else:
            components[root] &= w
    print(p, components)
    ans = []
    for a,b in query:
        x,y = find_parent(a), find_parent(b)
        if x != y:
            ans.append(-1)
        else:
            ans.append(components[x])
    return ans