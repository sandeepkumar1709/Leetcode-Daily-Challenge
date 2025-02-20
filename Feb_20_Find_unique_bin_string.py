"""
Approach:
    To solve this problem, I tried to find the binary string which is not present in the given list. since it been said that multiple answers are possible, 
    I just needed to find one. So I iterated from 0 to n+2 since the answer can be definitely between this range. I converted the number to binary and then
    checked if the binary string is present in the given list. If not then I returned the binary string.
Time Complexity:
    O(n^2) where n is the length of the list. one n is for iterating from 0 to n+2 and another n is for converting the number to binary.
Space Complexity:
    O(n) for storing the binary string.
"""



def findDifferentBinaryString(nums) -> str:
    n = len(nums)
    for i in range(n+2):
        bin_ = bin(i)[2:]
        check = '0'*(n - len(bin_)) + bin_
        if check not in nums:
            return check
print(findDifferentBinaryString(["01","10"])) # "00"