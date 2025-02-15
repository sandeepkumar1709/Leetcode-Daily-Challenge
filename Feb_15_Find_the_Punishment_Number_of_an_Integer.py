def check_punish_number(num, sum_, index, value):
    if index == len(num) and sum_ == value:
        return True

    for i in range(index,len(num)):
        sum_ = sum_ + int(num[index:i+1])
        if check_punish_number(num, sum_,i+1, value):
            return True
        sum_ -= int(num[index:i+1]) # Backtrack
    return False


def punishmentNumber(n: int) -> int:
    ans = 0
    for i in range(1,n+1):
        if check_punish_number(str(i*i),0,0,i):
            ans+=(i*i)
    return ans


print(punishmentNumber(1870)) # 18556601



"""
Time Complexity: O(n * 2^n) 
    where n is the input number, as we are checking all the possible combinations of numbers from 1 to n which is n complexity
    for each number we are checking all the possible combinations of the substrings of number which is 2^n complexity.

Space Complexity: O(1)
"""


