"""
Approach:
    This variation is interesting because solving this with binary serach made me think of the house robber problem.
    We use binary search to find the minimum capability, then we use a recursive function to check if it is possible to rob k houses with the given capability.T
Time Complexity:
    O(n log m) where n is the length of the nums array and m is the maximum number in the nums array.
Space Complexity:
    O(n) for the recursion stack in the worst case.

"""


def minCapability(nums, k: int) -> int:

    def isPossible(val, index, count):
        # print(val, index, count)
        if count == k:
            return True
        if index >= n:
            return False

        
        if nums[index] <= val:
            if isPossible(val, index+2,count+1):
                return True
        elif isPossible(val, index+1,count):
                return True
        return False



    low, high,n = min(nums), max(nums),len(nums)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if isPossible(mid,0,0):
            high = mid-1
            ans = mid
        else:
            low = mid+1
    return ans

# Example usage
print(minCapability([2,3,5,9], 2))  # Expected output: 5
print(minCapability([2,7,9,3,1], 2))  # Expected output: 2