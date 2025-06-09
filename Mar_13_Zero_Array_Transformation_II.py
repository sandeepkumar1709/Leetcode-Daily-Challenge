"""
Approach:
    Here 1st we need to be aware of the solving a problem using difference array. if we know how to solve a problem using difference array, 
    then we can use binary search to find the minimum number of queries required to make all elements of the array zero.
    We can use binary search to find the minimum number of queries required to make all elements of the array zero.
# Time Complexity:
    O(n log m) where n is the length of the nums array and m is the length of the queries array.
# Space Complexity:
    O(n) for the zero_array used to store the difference array.s
"""

def minZeroArray(nums, queries) -> int:
    
    def isPossible_query(queries_sub):
        zero_array = [0]*(n)
        for l,r,value in queries_sub:
            zero_array[l]+=value
            if r != n-1:
                # print(r,n)
                zero_array[r+1] -= value
        for i in range(1,n):
            zero_array[i] += zero_array[i-1]
        # print(zero_array,queries_sub)
        for i in range(n):
            if zero_array[i] < nums[i]:
                return False
        return True

    n = len(nums)
    # print
    low, high, ans = 0, len(queries),-1
    while low <= high:

        mid = (low+high) // 2
        # print(mid,low, high,n)
        if isPossible_query(queries[:mid]):
            ans = mid
            high = mid-1
        else:
            low = mid+1

    return ans


# Example usage
print(minZeroArray([1,2,3,4], [[0,1,2],[1,2,3],[0,3,1]]))  # Expected output: -1
print(minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))  # Expected output: 2