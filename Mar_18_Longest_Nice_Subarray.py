"""
Approach:
    This problem can be solved using a sliding window approach. We maintain a window of elements
    such that the bitwise AND of all elements in the window is 0. We expand the window by adding
    elements from the right if the bitwise AND condition is satisfied. If the condition is violated,
    By including the current element into the bitwise AND calculation and we shrink the window from the left 
    until the condition is satisfied again. We keep track of the maximum size of the window during this process.
Time Complexity:
    O(n) where n is the length of the nums array. Assuming each bitwise operation takes constant time.
Space Complexity:
    O(1) since we are using a constant amount of space.
"""

def longestNiceSubarray(nums) -> int:
    initial = nums[0]
    l,r,ans = 0,0,0
    for idx,r in enumerate(nums):
        while l!=idx and (initial & r) != 0:
            initial ^= nums[l] 
            l+=1
        initial |= r
        ans = max(ans, idx-l+1)
    return ans


# Example usage
print(longestNiceSubarray([1,3,8,48,10]))  # Expected output: 3
print(longestNiceSubarray([3,1,5,11,13]))  # Expected output: 1