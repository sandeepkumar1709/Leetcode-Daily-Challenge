"""
Approach:
    To check if the grid can be cut into sections, we need to check if there are at least 3 non-overlapping 
    intervals in either the x or y direction. We can do this by sorting the boundaries and then merging 
    overlapping intervals. If the number of non-overlapping intervals is greater than or equal to 3, 
    we can cut the grid into sections.

Time Complexity:
    O(nlogn) where n is the number of rectangles. We sort the boundaries and then merge them.
Space Complexity:
    O(n) where n is the number of rectangles. We store the boundaries in a list.
"""


def nonOverLap(boundaries):
    new_boundaries = []
    n,i = len(boundaries),0
    while i < n:
        start = boundaries[i][0]
        end = boundaries[i][1]
        while i+1 < n and end > boundaries[i+1][0]:
            
            end = max(end, boundaries[i+1][1])
            i+=1

        new_boundaries.append((start, end))
        i+=1

    return new_boundaries


def checkValidCuts(n: int, rectangles):
    x_boundaries, y_boundaries = [],[]
    for x1,y1,x2,y2 in rectangles:
        x_boundaries.append((y1,y2))
        y_boundaries.append((x1,x2))
    x_boundaries.sort()
    y_boundaries.sort()
    x_side,y_side = nonOverLap(x_boundaries), nonOverLap(y_boundaries)
    return len(x_side) >=3 or len(y_side) >= 3


print(checkValidCuts(4, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))

print(checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))