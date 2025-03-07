"""
Approach:
    I approached with pretty brute force approach, where I recursively check if the value is equal to n, if yes return True,
    also given the constraint that the maximum value of n is 10^7, I can check for the maximum bitcount of 15 since 3^15 is 14348907 ~ 10^7
    So, I can recursively check if the value is equal to n or not.
    If the value is greater than n or the bitcount is greater than 15, then return False.

Time complexity:
    O(2^n)
Space complexity:
    O(1)
"""


def checkPower(value,bitcount, current_power):
    # print(bitcount, current_power)
    if value > n or bitcount > 15:
        return False
    if value == n:
        return True

    if checkPower(value, bitcount+1, current_power*3) or checkPower(value + current_power, bitcount+1, current_power*3):
        return True

    return False





n = 13 # 3^2 + 3^1 + 3^0

print(checkPower(1,1,3) or checkPower(0,1,3)) # True