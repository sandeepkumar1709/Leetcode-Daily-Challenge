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