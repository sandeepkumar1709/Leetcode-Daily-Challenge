"""
Approach:
    To count the number of days without meetings, we can first get the non-overlapping intervals of meetings.
    Then we can count the number of days between these intervals which are not occupied by meetings.

Time Complexity:
    O(nlogn) where n is the number of meetings. We sort the meetings and then merge them.

Space Complexity:
    O(n) where n is the number of meetings. We store the merged meetings in a new array.
"""


def countDays(days: int, meetings) -> int:
    meetings.sort()
    new_arr,n = [],len(meetings)
    i = 0
    while i < n:
        start = meetings[i][0]
        end = meetings[i][1]
        while i+1 < n and end >= meetings[i+1][0]:
            end = max(end, meetings[i+1][1])
            i+=1
        new_arr.append((start, end))
        i += 1
    ans, i = new_arr[0][0]-1,0
    while i+1 < len(new_arr):
        ans += (new_arr[i+1][0] - new_arr[i][1]-1)
        i+=1
    ans += (days - new_arr[i][1])
    return ans


print(countDays(10, [[1,2],[2,3],[4,5],[6,7],[8,9]])) #expected 1
print(countDays(10, [[5,7],[1,3],[9,10]])) # expected 2