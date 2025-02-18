"""
Approach:
    To solve this problem, I first created a dictionary to track the number of consecutive D's and I's for each index.
    Then I created a list of numbers from 1 to 9 and I iterated through the pattern and for each index, I checked the
    if the pattern is "D" or "I" if it is "I" then I added the smallest number from the list and if it is "D" then I added
    count of 'D' number from the list. Finally, I added the last number from the list to the answer and returned the answer.
    e.g. if we have "DDDDDDDD" then each time we add count of 'D' from the list, for the 1st time we add index 8 from the list
    since we 8D's and then we add 7 from the list since we have 7D's and so on.

Time Complexity:
    O(n^2) where n is the length of the pattern, as we are iterating twice through the pattern to find the consecutive D's and I's.

space Complexity:
    O(n) where n is the length of the pattern, as we are storing the consecutive D's and I's in the dictionary.

"""


def smallestNumber(pattern: str) -> str:
    tracker = {}
    for i in range(len(pattern)):
        next_pattern, count = "", 0
        for j in range(i, len(pattern)):
            if i == j:
                next_pattern = pattern[j]
            if next_pattern != pattern[j]:
                break
            count+=1
        tracker[i] = str(count)+next_pattern
    list_to_put = list(range(1,10))
    answer_to_return = ""
    for i in range(len(pattern)):
        next_path = tracker[i]
        count = int(next_path[0])
        if next_path[-1] == "D":
            answer_to_return += str(list_to_put[count])
            list_to_put.pop(count)
        else:
            answer_to_return += str(list_to_put[0])
            list_to_put.pop(0)
    answer_to_return += str(list_to_put[0])
    return answer_to_return



print(smallestNumber("IDID")) # "13254"