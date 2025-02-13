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