"""
Approach:
    The approach is to iterate over the array and find the maximum ascending sum.
    The idea is to iterate over the array and find the maximum ascending sum by adding the current element to the sum if the current element is greater than the previous element.
    If the current element is less than the previous element, then update the maximum sum and reset the sum.
    Return the maximum sum.
Time complexity:
    O(n) - to iterate over the array.
Space complexity:
    O(1) - no extra space is used.
"""


def maxAscendingSum(nums) -> int:
    sum_var = 0
    temp_sum = nums[0]
    for i in range(1,len(nums)):
        # print(sum_var, temp_sum,i)
        if nums[i] > nums[i-1]:
            temp_sum+=nums[i]
        else:
            sum_var = max(sum_var, temp_sum)
            temp_sum = nums[i]
    return max(sum_var, temp_sum)

print(maxAscendingSum([10,20,30,5,10,50])) # 65