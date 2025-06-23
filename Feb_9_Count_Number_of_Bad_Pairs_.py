"""
Approach:
    I couldn't able to get the part until I saw the hint in the problem statement. 
    The hint suggests that we need to consider the difference between the value and its index. This means we can transform the array into a new array 
    where each element is the original element minus its index. Then, we can count the number of good pairs in this transformed array.
    (i.e. we need to check for good pairs first so get that we need to check for conditionn nums[j] -nums[i] == j - i, 
    we can rearrange this to nums[j] - j == nums[i] - i)
Time complexity:
    O(n) - we iterate through the array once to create the transformed array and then again to count the good pairs.
Space complexity:
    O(n) - we use a dictionary to count the occurrences of each transformed value.
"""


def countBadPairs(nums) -> int:

    counter = {}

    for i in range(len(nums)):
        nums[i] = nums[i] - i
    
    n = len(nums)
    total_comb = (n * (n-1))//2

    good = 0

    for i in nums:
        counter[i] = counter.get(i,0)
        # good += counter[i]
        counter[i] += 1
    
    for i in counter:
        good += (counter[i] * (counter[i]-1))//2

    return total_comb - good


print(countBadPairs([4,1,3,3])) #5