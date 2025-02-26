"""
Approach:
    At each index we can store the sum of all elements from 0 to that index. We can then check if the sum is odd or even.
    So at each index i if the prefix sum is even then we can add the number of odd prefix sums till now to the answer.
    If the prefix sum is odd then we can add the number of even prefix sums till now to the answer. 
    
    This is because we need to find the number of subarrays with odd sum and when we know that odd sum - even sum we get odd sum. 
    so at that index we just remove even sums and the result will b odd sum

Time Complexity: O(n)
Space Complexity: O(1)



"""


def numOfSubarrays(arr) -> int:

    var_sum = 0

    for idx, num in enumerate(arr):
        var_sum += num
        arr[idx] = var_sum

    odd, even = 0,0
    ans = 0
    for i in arr:
        if i%2 == 0:
            ans= (ans + odd) % 1000000007
            even+=1
        else:
            ans=(ans+even)% 1000000007
            odd+=1
            ans+=1
        # print(ans,i)
    return ans
    
print(numOfSubarrays([1,3,5])) # 4
print(numOfSubarrays([2,4,6])) # 0