"""
Approach:
    This problem can be solved with slight modification of Dijkstra's algorithm.
    We will use a priority queue to keep track of the minimum distance to each node and the number of ways to reach that node.
    If we find a shorter path to a node, we update the distance and the number of ways. 
    if we find a path with the same distance, we add the number of ways from the current node to the number of ways to reach that node.
    
    
Visualization: 
    We can assume this as, let say we are reaching node A from node B and that is the shortest path that we have encountered so far,
    then we can say that the number of ways to reach node A is equal to the number of ways to reach node B.
    Now if we encounter another path to node C from node B with the same distance, the number of ways to reach node B will be 
    number of ways to reach node C + the number which is already there in the number of ways to reach node B.
Time complexity:
    O(m log m + n) where n is the number of nodes and m is the number of edges, 
    insertion and deletion in the priority queue takes O(log m) time and at max we can insert and delete m edges
Space complexity:
    O(n + m) for the graph and the priority queue. 
"""


import heapq
def countPaths( n, roads) -> int:

    graph = [[] for _ in range(n)]
    mod = 1000000007
    for u,v,time in roads:
        graph[u].append((v,time))
        graph[v].append((u,time))

    heap = [(0,0)]
    dist = [float('inf')]*(n)
    dist[0] = 0
    ways = [0]*(n)
    ways[0] = 1
    while heap:
        distance, node = heapq.heappop(heap)
        for each_node, time in graph[node]:
            if dist[each_node] > time + distance:
                dist[each_node] = time + distance
                ways[each_node] = (ways[node]) % mod
                heapq.heappush(heap, (dist[each_node], each_node ))
            elif dist[each_node] == time + distance:
                ways[each_node] = (ways[each_node] + ways[node]) % mod
    # print(ways)
    return ways[n-1]
