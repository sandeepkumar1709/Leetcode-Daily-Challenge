"""
Approach:
    This can solved by simple brute force, but it is asked to solve in O(log n) time.
    We can use binary search to find the index of the first positive number and the index of the last negative number.
    Then we can calculate the count of positive and negative numbers based on these indices, if both indices are found.
    else we can return the count based on the indices found.
# Time Complexity:
    O(log n) for binary search to find the indices.
# Space Complexity:
    O(1) since we are not using any extra space.
"""
def maximumCount(nums) -> int:
    
    
    def getPosIndex():
        low, high,index = 0,n-1,-1
        while low <= high:
            mid = (low + high)//2
            # print(mid)
            if nums[mid] > 0:
                index = mid
                high = mid-1
            else:
                low = mid+1
        return index
    
    def getNegIndex():
        low, high,index = 0,n-1,-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] < 0:
                index = mid
                low = mid+1
            
                
            else:
                high = mid-1
        return index
    n = len(nums)
    posIndex, negIndex = getPosIndex(), getNegIndex()
    # print(posIndex, negIndex)
    if posIndex == -1 and negIndex == -1:
        return 0
    if negIndex == -1:
        return n-posIndex
    if posIndex == -1:
        return negIndex+1
    return max(negIndex+1, n-posIndex)

# Example usage
print(maximumCount([-2,-1,0,1,2]))  # Expected output: 2 (negatives: -2, -1; positives: 1, 2)
print(maximumCount([-3,-2,-1,0,1,2,3]))  # Expected output: 3 (negatives: -3, -2, -1; positives: 1, 2, 3)