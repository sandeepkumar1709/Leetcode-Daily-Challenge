"""
Approach:
    We will use a while loop to repeatedly remove the first occurrence of the substring `part` from the string `s`  
    until `part` is no longer found in `s`.
Time complexity:
    O(n * m) where n is the length of s and m is the length of part, in the worst case we may have to remove part from s n/m times.
Space complexity:
    O(1) - no extra space is used.
"""


def removeOccurrences(s: str, part: str) -> str:
    while len(s) > 0 and part in s:
        s = s.replace(part,"",1)
    return s
print(removeOccurrences("daabcbaabcbc","abc")) #dab