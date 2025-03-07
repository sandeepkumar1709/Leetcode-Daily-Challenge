"""
Approach:
    The approach is to find the pattern, 
    when we have a 1x1 grid, there is only 1 colored cell, 
    when we have a 2x2 grid, we have 1 at the top and 3 in the middle and mirror 1 at the bottom,
    when we have a 3x3 grid, we have 1, 3 at the top and 5 in the middle and mirror 3, 1 at the bottom,
    when we have a 4x4 grid, we have 1, 3, 5 at the top and 7 in the middle and mirror 5, 3, 1 at the bottom,
    when we have a 5x5 grid, we have 1, 3, 5, 7 at the top and 9 in the middle and mirror 7, 5, 3, 1 at the bottom,
    and so on.
    So, the pattern is 2 * ((n-1) * (n-1)) + (2 * n) -1
Time complexity:
    O(1)
Space complexity:
    O(1)
"""


def coloredCells(n: int) -> int:
        return 2 * ((n-1) * (n-1)) + (2 * n) -1



print(coloredCells(5)) # 41