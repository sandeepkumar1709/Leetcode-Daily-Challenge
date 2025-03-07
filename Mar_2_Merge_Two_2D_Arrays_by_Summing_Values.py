"""
Approach:
    The approach is to use a dictionary to store the values of the first array.
    Then iterate over the second array and check if the value is present in the dictionary.
    If it is present, add the values and update the dictionary value to -1.
    Finally, iterate over the dictionary and add the values which are not -1 to the answer.
Time complexity:
    O(n)
Space complexity:
    O(n)
"""


def mergeArrays(nums1, nums2):

    merged = {}
    for a,b in nums1:
        merged[a] = b

    ans = []
    for a,b in nums2:
        temp_ans = b
        if a in merged:
            temp_ans += merged[a]
            merged[a] = -1
        ans.append([a, temp_ans])

    for ele in merged:
        if merged[ele] != -1:
            ans.append([ele, merged[ele]])
    return sorted(ans)


nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1,4],[3,2],[4,1]]
print(mergeArrays(nums1, nums2)) # [[1, 6], [2, 3], [3, 2], [4, 6]]