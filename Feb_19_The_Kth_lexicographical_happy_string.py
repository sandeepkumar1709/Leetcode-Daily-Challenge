"""
Approach:
    To solve this problem, I first created a dictionary to track the next element for each element. Then I created a recursive function
    to find the kth happy string. I started with the first element and then recursively called the function with the next element(here I tried optimizing 
    by picking next character lexicographically smaller string, e.g. if current charater is 'a', then I tried appending 'b' for recursive call if current 
    string 'b' I appened 'a' for next recursive call) and     I kept track of the number of happy strings found so far. If the number of happy strings 
    found so far is equal to k then I returned     the current string. If not then I called the function with the next element and so on. Finally, 
    I returned the string found, if not found then I returned an empty string.


Time Complexity:
    O(2^n) where n is the length of the string, as we are recursively calling the function twice for each element.

space Complexity:
    O(n) here one n is recursive depth and another n is the space we maintain for current string.
"""





def kthHappyString(curr, next_element, tracker,n,k):
    if len(curr) == n:
        tracker[0]+=1
        if tracker[0] == k:
            return curr
        return ""


    value_1 =  kthHappyString(curr+next_element[curr[-1]][0], next_element,tracker,n,k)
    if len(value_1) >= 1:
        return value_1

    value_2 = kthHappyString(curr+next_element[curr[-1]][1], next_element,tracker,n,k)

    if len(value_2) >= 1:
        return value_2
    return ""


def getHappyString(n: int, k: int) -> str:
    next_element = {'a':['b','c'], 'b':['a','c'], 'c':['a','b']}
    position = [0]
    for string in ['a','b','c']:
        return_string = kthHappyString(string,next_element, position, n,k)
        if return_string != "":
            return return_string
    return ""

print(getHappyString(3,9)) # "cab"
print(getHappyString(1,3)) # "c"