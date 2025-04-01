"""
Approach: 
    To get the minimum operations to make the grid uni-value, we use the median of the grid values 
    because the median is the balanced point that minimizes the sum of absolute deviations.
    So the problem boils down to finding the median of the grid values and then calculating the
    number of operations needed to make all values equal to the median. To that we flatten the grid
    and sort it, then we can find the median by taking the middle two elements.
    We then calculate the number of operations needed to make all values equal to the median by
    checking if the absolute difference between each value and the median is divisible by x. If it is not,
    we return -1. If it is, we calculate the number of operations needed to make all values equal to the median


Time Complexity:
    O(nlogn) where n is the number of elements in the grid. We sort the grid values to find the median.
Space Complexity:
    O(n) where n is the number of elements in the grid. We store the grid values in a list.
    We also use a few variables to store the median and operations, but they are constant space.

"""



def getop(value, straight_list, x):
    operations = 0
    for i in straight_list:
        if abs(value-i) % x != 0:
            return -1
        operations +=  abs(value-i) // x
    # print(value, operations)
    return operations

def minOperations(grid, x):
    straight_list = []
    for i in grid:
        straight_list.extend(i)
    straight_list.sort()
    n = len(straight_list)

    median_1, median_2 = n//2, (n//2)-1

    ans_1, ans_2 = getop(straight_list[median_1], straight_list,x), getop(straight_list[median_2], straight_list,x)
    if ans_1 == -1:
        return ans_2
    if ans_2 == -1:
        return ans_1
    return min(ans_1, ans_2)


print(minOperations([[2,4],[6,8]], 2)) # Expected output: 4
print(minOperations([[1,2,3],[4,5,6],[7,8,9]], 1)) # Expected output: 12