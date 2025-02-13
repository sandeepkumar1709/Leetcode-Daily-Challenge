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