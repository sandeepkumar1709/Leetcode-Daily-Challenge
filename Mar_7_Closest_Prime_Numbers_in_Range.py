
"""
Approach:
    The approach is to use the Sieve of Eratosthenes to find the prime numbers in the range.
    Then iterate over the range and find the closest prime numbers by finding the minimum difference between the prime numbers.

Time complexity:
    O(nlog(log(n)) + right-left) - O(nlog(log(n))) for finding the prime numbers and O(right-left) for finding the closest prime numbers.
Space complexity:
    O(right) - to store the prime numbers.



## 2 main things in Sieve of Eratosthenes:
    1. Why the first loop is iterating till sqrt(n) and not n? => Because let us take an example of 36 => 
        Assume we marked until 6 now for 7 we do 7*2, 7*3, 7*4, 7*5, 7*6 but if you correctly observe 7*2 is already marked by 2*7, similarly 7*3 is already marked by 3*7
        so no need to mark it again. we can stop at sqrt(n) because after that all the numbers will be already marked by the previous numbers.
    2. Why the second loop is starting from i*i and not i*2? => Because let us take an example of 100 => 
        Now assume 1st loop iterated until 5, now for 5*2 we already covered it when outer loop is at 2, so no need to mark it again.
        Similarly for 5*3 we already covered it when outer loop is at 3, so no need to mark it again. So we can start from i*i.
        This continues until i^2 because all the numbers will be already marked by the previous numbers.
        So we need to start from i*i.
"""


def closestPrimes(left: int, right: int):
        end = right + 10
        visited = [False] * end
        i = 2
        while i*i < end:
            if not visited[i]:
                counter = 2
                for j in range(i*i, end, i):
                    visited[j] = True
            i+=1
        ans = [-1,-1]
        # print(prime)
        visited[1] = True
        diff = float('inf')
        curr = float('-inf')
        for i in range(left, right+1):
            if not visited[i]:
                temp_diff = i-curr
                if temp_diff < diff:
                    # print(temp_diff, diff)
                    diff = temp_diff
                    ans = [curr,i]
                    # print(ans)
                curr = i
        return ans

print(closestPrimes(10, 20)) # [11, 13]