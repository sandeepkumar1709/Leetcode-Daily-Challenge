"""
Approach:
    The approach is to use a hashmap to store the sum of digits and the numbers that have that sum.
    Then iterate over the hashmap and if the length of the list of numbers with the same sum is greater than 1, 
    then we can find the maximum sum of two numbers with the same sum of digits. 
    for sort we can use bisect.insort to keep the list sorted.
Time complexity:
    O(n log n) - to insert elements in the sorted order using bisect.
Space complexity:
    O(n) - to store the elements in the hashmap.
"""

def sum_of_digits(num):
        ans = 0
        while num > 0:
            ans += (num%10)
            num = num//10
        return ans
import bisect

def maximumSum(nums) -> int:
    

    digit_map = {}

    for i in nums:
        s = sum_of_digits(i)
        if s in digit_map:
            bisect.insort(digit_map[s], i)
        else:
            digit_map[s] = [i]

    ans = -1
    # print(digit_map)
    for i in digit_map:
        if len(digit_map[i]) > 1:
            ans = max(ans, digit_map[i][-1] + digit_map[i][-2])
    return ans


print(maximumSum([55, 23, 123, 77, 99, 79, 123, 55])) # 246