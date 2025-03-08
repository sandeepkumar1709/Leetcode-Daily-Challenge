"""
Approach:
    The approach is to use a hashmap to store the product of the elements and the number of times they occur.
    Then iterate over the hashmap and if the number of times an element occurs is greater than 1, then find the number of combinations of selecting 2 elements from the number of times the element occurs.
    which means we got number of elements which has a tuple that satisfies the condition now as per the question if there is bipair 
    which has a*b = c*d then we can form 8 tuples(i.e. (a,b,c,d), (a,c,b,d), (a,d,b,c), (b,c,a,d), (b,d,a,c), (c,d,a,b), (c,d,b,a), (d,b,c,a))
    so we need to find the number of such tuples and return the count.
Time complexity:
    O(n^2) - to iterate over the elements.
Space complexity:
    O(n) - to store the elements.
"""

def tupleSameProduct(nums) -> int:
    def get_2_combinations(temp):
        return (temp * (temp -1)) //2

    elements = {}

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            number = nums[i] * nums[j]
            elements[number] = elements.get(number, 0) + 1
    # print(elements)
    ans = 0
    for i in elements:
        if elements[i] > 1:
            ans += (get_2_combinations(elements[i]) * 8)
    return ans

print(tupleSameProduct([2,3,4,6])) # 8

#time complexity is O(n^2) and space complexity is O(n)