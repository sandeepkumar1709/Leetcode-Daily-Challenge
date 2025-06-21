"""
Approach:
    The approach is to use BFS to traverse the graph and count the number of nodes and edges in each connected component.
    The graph is complete if the number of edges is equal to (nodes * (nodes - 1)) // 2. 
    We apply BFS for each unvisited node and check if the component is complete.
Time complexity:
    O(n + m) where n is the number of nodes and m is the number of edges.
Space complexity:
    O(n + m) for the graph and visited list.
"""


from collections import deque
def countCompleteComponents(n: int, edges):

    def bfs(start_node):
        queue = deque([start_node])
        node_set, edges = set(), set()
        while queue:
            node = queue.popleft()
            node_set.add(node)
            if not visited[node]:
                visited[node] = True
                for each_node in graph[node]:
                    queue.append(each_node)
                    if (node,each_node) not in edges and (each_node,node) not in edges:
                        edges.add((node,each_node))
        # print(node_set, edges)
        return len(node_set), len(edges)

    graph = [[] for _ in range(n)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False]* (n)
    ans = 0
    for i in range(n):
        if not visited[i]:
            nodes, edges = bfs(i)
            # print(nodes, edges, edges == ((nodes * (nodes-1)) // 2))
            if edges == ((nodes * (nodes-1)) // 2):
                ans+=1
    return ans