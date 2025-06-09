"""
Approach:
    This problem can be solved by counting the frequency of each number in the array.
    If all numbers have even frequency, then we can divide the array into pairs.
# Time Complexity:
    O(n) where n is the length of the nums array.
# Space Complexity:
    O(n) for the counter dictionary to store the frequency of each number.
"""

def divideArray( nums) -> bool:
    counter = {}
    for i in nums:
        counter[i] = counter.get(i,0) +1
    for num in counter:
        if counter[num] %2 != 0:
            return False
    return True

# Example usage
print(divideArray([3,2,3,2,2,2]))  # Expected output: True