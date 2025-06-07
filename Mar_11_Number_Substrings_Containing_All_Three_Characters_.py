"""
Approach:
    To count the number of substrings that contain all three characters 'a', 'b', and 'c', we can use a sliding window approach.
    We maintain a counter for the characters and expand the right end of the window until we have all three characters, 
    then we count the valid substrings that can be formed with the current left pointer (i.e., with left pointer fixed, all the substrings from there since we got the valid string).
    After counting, we move the left pointer to shrink the window until we no longer have all three characters.
Time Complexity:
    O(n) where n is the length of the string. We iterate through the string once or at most twice.
Space Complexity:
    O(1) since we are only using a fixed-size counter for the characters 'a', 'b', and 'c'.
"""

def numberOfSubstrings(s: str) -> int:
    def allThere(counter):
        return counter['a'] >= 1 and counter['b'] >= 1 and counter['c'] >= 1 
    counter = {'a':0, 'b':0,'c':0}
    left,right = 0,0
    ans,n = 0, len(s)
    
    while right < n:
        counter[s[right]]+=1
        while allThere(counter):
            ans += (n-right)
            counter[s[left]]-=1
            left+=1
        right+=1
    return ans


print(numberOfSubstrings("abcabc"))  # Example usage, should return 10
print(numberOfSubstrings("aaacb"))   # Example usage, should return 3