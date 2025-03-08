"""
Approach:
    The approach is to use a sliding window technique to find the minimum recolors.
    The idea is to iterate over the first k elements and find the number of white blocks.
    Then iterate over the remaining elements and find the minimum recolors by sliding the window.
    The minimum recolors can be found by finding the minimum of the current minimum recolors and the current number of white blocks.
    Return the minimum recolors.
Time complexity:
    O(n) - to iterate over the blocks.
Space complexity:
    O(1) - no extra space is used.
"""


def minimumRecolors(blocks: str, k: int) -> int:
    i,ans_pointer = 0,0
    while i<k:
        if blocks[i] == 'W':
            ans_pointer+=1
        i+=1
    ans = ans_pointer
    start = 0
    while i < len(blocks):
        if blocks[start] == 'W':
            ans_pointer-=1
        if blocks[i] == 'W':
            ans_pointer+=1
        start += 1
        i+=1
        ans = min(ans,ans_pointer)
    return ans

print(minimumRecolors("BBWBWBWB", 3)) # 1