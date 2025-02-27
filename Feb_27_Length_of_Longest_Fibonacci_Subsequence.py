"""
Approach:
    Intial thought is to iterate all the pairs and for each pair, try checking finnocci sequence length and update the max length.
    This will take O(n^2*Log(n)) time because the we kind of doubling the next element since it is fibonacci sequence.

    Now, let us take sequence of length 3, [1, 2, 3]. for pair (1,2), we can find 3, we get some answer. Now, pairing with 2 we get pair (2,3), 
    which we would have already checked. So we can memorize that result, so we can use DP to solve it

Time Complexity: O(n^2)

Space Complexity: O(n^2)

"""




def lenLongestFibSubseq(arr) -> int:
    n = len(arr)
    arr_map = {}
    for idx, num in enumerate(arr):
        arr_map[num] = idx
    dp = [[0] *n for _ in range(n)]
    ans_ret = 0


    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            next_val = arr[i] + arr[j]
            if next_val in arr_map:
                k = arr_map[next_val]
                dp[i][j] = 1+dp[j][k]
                ans_ret = max(ans_ret, 1+dp[j][k])
            else:
                dp[i][j] = 2


    return ans_ret



print(lenLongestFibSubseq([1,2,3,4,5,6,7,8])) # 5
    