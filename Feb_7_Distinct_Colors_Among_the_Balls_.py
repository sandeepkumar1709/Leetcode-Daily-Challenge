"""
Approach:
     We maintain 2 dictionaries:
     1. slot: to keep track of the color of each ball at a given slot
     2. color_counter: to count the occurrences of each color
     Now if a ball is added to a slot, we check if the slot already has a color. If it does, we decrement the count of that color in color_counter. 
     if the count becomes zero, we remove that color from color_counter. Then we update the slot with the new color and increment the count of that color in color_counter. 
       Then the length of color_counter gives us the number of distinct colors at that point.

Time Complexity: O(1) for each query, since insertion and deletion in dictionaries are average O(1) operations.
Space Complexity: O(n) for storing the colors in the slot and their counts in color_counter

"""

from collections import defaultdict




def queryResults(limit: int, queries):
        slot, color_counter,ans = {}, defaultdict(int),[]
        for num, color in queries:
            if num in slot:
                color_counter[slot[num]]-=1
                if color_counter[slot[num]] == 0:
                    del color_counter[slot[num]]
            slot[num] = color
            color_counter[color] +=1
            ans.append(len(color_counter))
        return ans



print(queryResults(4, [[0,1],[1,2],[2,2,],[3,4],[4,5]])) #[1,2,2,3,4]