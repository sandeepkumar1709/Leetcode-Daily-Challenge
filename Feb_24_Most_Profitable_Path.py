

"""
Approach:
    We can use DFS to find the path from Bob to the root and store the time at which Bob will reach each node in a dictionary.
    Then we can use BFS to traverse the tree and calculate the maximum profit at each node, taking into account Bob's path.
    We can keep track of the maximum profit at each node and return the maximum profit at the leaf nodes.

Time Complexity: O(n) # For DFS and BFS 
Space Complexity: O(n)
"""

from collections import deque

def bob_path(source, prev, time):
    if source == 0:
        bob_parent[source] = time
        return True

    for children in graph[source]:
        if children == prev:
            continue
        # if source != prev:
        
        if bob_path(children, source, time+1):
            bob_parent[source] = time
            return True
    return False

def bfs_to_get_profit():

    q = deque([(0,-1,0, amount[0])])
    ans = float('-inf')
    while q:
        node, parent, time, profit = q.popleft()
        for children in graph[node]:
            if children != parent:
                curr_profit = amount[children]
                if children in bob_parent:
                    if time +1 > bob_parent[children]:
                        curr_profit = 0
                    if time + 1 == bob_parent[children]:
                        curr_profit = curr_profit //2
                q.append((children, node, time+1, profit+curr_profit))
                if len(graph[children]) == 1:
                    ans = max(ans, profit+curr_profit)

    return ans

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

n = len(amount)
graph = [[] for _ in range(n)]

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

bob_parent = {}
bob_path(bob,-1,0)
print(bfs_to_get_profit()) # 6