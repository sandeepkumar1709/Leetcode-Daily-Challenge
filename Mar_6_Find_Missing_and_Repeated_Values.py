"""
Approach:
    Brute force approach is to iterate over the grid and find the repeated and missing values by using a set.
Time complexity:
    O(n^2)
Space complexity:
    O(n^2)
"""

def findMissingAndRepeatedValues(grid):
    n = len(grid)
    ans = []
    visited = set()
    for row in grid:
        for ele in row:
            if ele in visited:
                ans.append(ele)
            else:
                visited.add(ele)
    for i in range(1, (n*n) +1):
        if i not in visited:
            ans.append(i)
            return ans
        
grid = [[1, 2, 3], [4, 9, 6], [8, 7, 9]]
print(findMissingAndRepeatedValues(grid)) # [9,5]