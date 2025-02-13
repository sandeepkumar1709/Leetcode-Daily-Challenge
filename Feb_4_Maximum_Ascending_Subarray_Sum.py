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