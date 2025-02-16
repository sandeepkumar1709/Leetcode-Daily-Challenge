"""
Approach:
    This is a very interesting problem, I enjoyed solving this problem, I tried using backtracking to solve this problem, 
    one small optimization I could do is using backtracking + Greedy approach, where I am trying to fill the array from maximum number to minimum number,
    So that the 1st valid sequence I get is the lexicographically largest valid sequence and I could simply return that sequence without checking for other sequences.
Time Complexity: 
    O(n!) where n is the input number, as we are checking all the possible combinations of numbers from 1 to n which is n! complexity.
Space Complexity: 
    O(n) where n is the input number, as we are using a visited array of size n and an ans array of size 2*n-1.
"""


def get_available_index(arr):
    for i in range(len(arr)):
        if arr[i] == -1:
            return i
    return -1
def all_visited(visited):
    for i in range(1, len(visited)):
        if visited[i] == False:
            return False
    return True
def subset(visited, ans, n, ans_length):
    available_index = get_available_index(ans)
    if available_index == -1:
        return ans
    
    for i in range(n,0,-1):
        other_side = available_index+i if i != 1 else available_index
        if visited[i] == False and other_side < len(ans) and ans[other_side] == -1:
            ans[available_index] = i
            ans[other_side] = i
            visited[i] = True
            sequence = subset(visited, ans, n, ans_length)
            if sequence != -1:
                return sequence
            ans[available_index] = -1
            ans[other_side] = -1
            visited[i] = False

    return -1


if __name__ == "__main__":
    n = 12
    visited = [False] * (n+1)
    ans = [-1] * ((2*n)-1)
    print(subset(visited, ans, n, len(ans))) #[12, 10, 11, 7, 5, 3, 8, 9, 3, 5, 7, 10, 12, 11, 8, 6, 9, 2, 4, 2, 1, 6, 4]




