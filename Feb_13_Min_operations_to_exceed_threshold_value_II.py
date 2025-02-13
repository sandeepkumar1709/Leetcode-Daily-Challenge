import heapq
def minOperations(nums, k: int) -> int:
    heapq.heapify(nums)
    counter = 0
    while len(nums) >= 2 and nums[0] < k:
        min_num = heapq.heappop(nums)
        max_num = heapq.heappop(nums)

        value = min_num *2 + max_num

        heapq.heappush(nums, value)
        counter+=1
    return counter
    

print(minOperations([1,2,3,4,5], 5)) # 3