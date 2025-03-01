"""
Approach:
    Brute force approach works here. We can iterate through the array and check if the current element is same as next element, 
    then we can double the current element and make next element as 0.
"""

def applyOperations(nums):

    n = len(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    ans = []
    for i in nums:
        if i != 0:
            ans.append(i)
    ans.extend([0]*(n-len(ans)))
    return ans
    

print(applyOperations([1,2,3,4])) # [1,2,3,4]
print(applyOperations([1,1,2,3])) # [2,3,0,0]