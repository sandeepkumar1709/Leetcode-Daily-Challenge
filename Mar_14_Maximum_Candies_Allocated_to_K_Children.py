"""
Approach:
    This problem can be solved using binary search. We can use binary search to find the maximum number of candies that can be allocated to each child.
    We can check if it is possible to allocate a certain number of candies to each child by dividing the total number of candies by the number of children.
# Time Complexity:
    O(n log m) where n is the length of the candies array and m is the maximum number of candies in the array.  
# Space Complexity:
    O(1) since we are not using any extra space.
"""

def maximumCandies(candies, k: int) -> int:

    def isPossible(val):
        count = 0
        for i in candies:
            count += (i//val)
        if count >= k:
            return True
        return False

    low, high,ans = 1, max(candies),0
    while low <= high:
        mid = (low + high)//2
        if isPossible(mid):
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans

# Example usage
print(maximumCandies([5,8,6], 3))  # Expected output: 5
print(maximumCandies([2,5], 11))  # Expected output: 0