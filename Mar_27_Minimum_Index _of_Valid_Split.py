"""
Approach:
  The idea is to maintain maximum frequency of each index in the prefix and suffix of the array.
    We can use a dictionary to store the frequency of each element in the prefix and suffix.
    At each index, we can check if the maximum frequency of the prefix and suffix is equal and dominant.
Time Complexity:
    O(n) where n is the length of the input array.
Space Complexity:
    O(n) where n is the length of the input array.
    We are using two dictionaries to store the frequency of each element in the prefix and suffix.
    So, the space complexity is O(n).
"""

from collections import defaultdict
def minimumIndex(nums):
    front_max, curr_max, curr_element = [], 0,-1
    frequency = defaultdict(int)
    for i in nums:
        frequency[i] +=1
        if frequency[i] > curr_max:
            curr_element = i
            curr_max = frequency[i]
        front_max.append((curr_max, curr_element))
    back_max, curr_max, curr_element = [], 0,-1
    frequency = defaultdict(int)

    for i in range(len(nums)-1,-1,-1):
        frequency[nums[i]] +=1
        if frequency[nums[i]] > curr_max:
            curr_element = nums[i]
            curr_max = frequency[nums[i]]
        back_max.append((curr_max, curr_element))
    back_max = back_max[::-1]
    n = len(nums)
    for i in range(len(nums)-1):
        if front_max[i][1] == back_max[i+1][1]:
            front_freq = front_max[i][0]
            back_freq = back_max[i+1][0]
            if (front_freq > (i+1) //2) and (back_freq > (n-i-1)//2):
                return i
    return -1


print(minimumIndex([2,2,2,1,2,5,5,2])) # Expected output: 0
print(minimumIndex([1,2,3,4,5,6])) # Expected output: -1