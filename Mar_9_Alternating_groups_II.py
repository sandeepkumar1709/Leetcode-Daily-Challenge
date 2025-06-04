"""
Approach:
    To count the number of alternating groups of size k, for circles with colors, we can extend the colors
    by repeating the first k-1 colors at the end. To find the number of alternating groups, we can iterate through the colors
    and keep track of the last index where the color was different from the previous one. If the current index minus the last index is greater than or equal to k,
    we can increment the count of alternating groups.
Time Complexity:
    O(n) where n is the length of the colors array. We iterate through the colors array once or at max twice.
Space Complexity:
    O(n) where n is the length of the colors array. We create a new array that is at most 2n in size.
"""


def numberOfAlternatingGroups(colors, k: int):

    for i in range(k-1):
        colors.append(colors[i])
    left,ans = 0,0
    for i in range(1, len(colors)):

        if colors[i] == colors[i-1]:
            left = i
        if i-left+1 >= k:
            ans+=1
    return ans


print(numberOfAlternatingGroups([1, 2, 1, 2, 1], 2))  # expected 4