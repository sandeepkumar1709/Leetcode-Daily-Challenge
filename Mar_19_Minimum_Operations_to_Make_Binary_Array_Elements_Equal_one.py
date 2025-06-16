"""
Approach:
    This problem can be solved by iterating through the array and flipping the next two elements
    whenever we encounter a 0. We keep track of the number of flips made. If we reach the end of the
    array and there are still 0s left, we return -1.
Time Complexity:
    O(n) where n is the length of the nums array.
Space Complexity:
    O(1) since we are using a constant amount of space.
"""

def minOperations(nums) -> int:
    flip = [1,0]
    counter = 0
    for l in range(len(nums)):
        if nums[l] == 0:
            if l >= len(nums)-2:
                return -1
            nums[l+1] = flip[nums[l+1]]
            nums[l+2] = flip[nums[l+2]]
            counter += 1
    return counter


# Example usage
print(minOperations([0,1,1,1,0,0]))  # Expected output: 3
print(minOperations([0,1,1,1]))  # Expected output: -1