"""
Approach:
    This is a variation of Kadane's algorithm. We can keep track of the maximum and minimum sum subarrays ending at each index.
    The maximum absolute sum will be the maximum of the absolute values of these sums.

Time Complexity: O(n)
Space Complexity: O(1)

"""


def maxAbsoluteSum(nums) -> int:
    max_sum, min_sum = float('-inf'), float('inf')

    curr_max, curr_min = 0,0

    for i in nums:
        curr_max+=i
        curr_min+=i

        curr_max = max(0, curr_max)
        curr_min = min(0, curr_min)

        max_sum = max(max_sum, curr_max)
        min_sum = min(min_sum, curr_min)

    return max(max_sum, abs(min_sum))

nums = [1,-3,2,3,-4]
print(maxAbsoluteSum(nums)) # 5
    