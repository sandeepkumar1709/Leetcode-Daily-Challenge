"""
Approach:
    This is a Bottom-up approach, try to do same as how we approach for the Longest Common Subsequence. we maintain a dp array of size n+1 and m+1.
    dp[i][j] represents the shortest common supersequence of str1[:i] and str2[:j]. 
    We fill the dp in just a way that at point i,j if str1[i] == str2[j] we need to look for top-left cell and add str1[i] to the answer.
    If str1[i] != str2[j] then we need to look for the cell which has the minimum length between top cell and left cell 
    and add the character which is not equal to the current character.
Time complexity:
    O(n*m)
Space complexity:
    O((n*m)^(n+m)) - So the DP array will be of size n*m and each cell will have a string of length n+m.

Below is the dry run of the code for the input str1 = "abac" and str2 = "cab"
    |_______c_______a_______b
	|""	    c	    ca	    cab
a	|a	    ac	    ca	    cab
b	|ab	    abc	    cab	    cab
a	|aba	abca	abca	caba
c	|abac	abac	abcac	cabac


One space optimized approach is to use only 2 rows instead of n rows.
We always need the previous row to calculate the current row. So we can use only 2 rows to store the values.
We can use the same approach as above but we need to maintain 2 rows instead of n rows.

Space complexity:
    O(2*n*m)


"""


def shortestCommonSupersequence(str1: str, str2: str) -> str:
    n = len(str1)
    m = len(str2)

    dp = [["" for _ in range(m+1)] for _ in range(2)]

    for i in range(m):
        dp[0][i+1] = str2[:i+1]

    # dp[1][1] = str1[1]

    up, down = 0,1
    for i in range(n):
        if i %2 == 0:
            up, down = 0,1
        else:
            up, down = 1,0
        dp[down][0] = str1[:i+1]
        for j in range(1,m+1):
            if str1[i] == str2[j-1]:
                dp[down][j] = dp[up][j-1]+str1[i]
            elif len(dp[up][j]) < len(dp[down][j-1]):
                dp[down][j] = dp[up][j]+str1[i]
            else:
                dp[down][j] = dp[down][j-1]+str2[j-1]
    return dp[down][-1]


print(shortestCommonSupersequence("abac", "cab")) # "cabac"