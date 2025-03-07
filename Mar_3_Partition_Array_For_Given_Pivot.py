
"""
Approach: 
    The approach is to iterate through the array and check if the current element is less than the pivot, then add it to the start of the array
    and if the current element is greater than the pivot, then add it to the end of the array to maintain the order.
    If the current element is equal to the pivot, then skip it.
    At the end, fill the remaining elements with the pivot.
Time complexity:
    O(n)
Space complexity:
    O(n)
"""


def pivotArray(nums, pivot: int):
    n = len(nums)
    ans = [0] * n
    start, end = 0, n-1
    start_counter,  end_counter = 0,n-1
    while start_counter < n and start <= end and end_counter >= 0:
        if nums[start_counter] < pivot:
            ans[start] = nums[start_counter]
            start+=1
        if nums[end_counter] > pivot:
            ans[end] = nums[end_counter]
            end-=1
        end_counter-=1
        start_counter+=1
    
    while start <= end:
        ans[start] = pivot
        start +=1
    return ans

print(pivotArray([5,2,4,4,6,4,4,3], 4)) # [2,3, 4, 4, 4, 4, 5, 6]