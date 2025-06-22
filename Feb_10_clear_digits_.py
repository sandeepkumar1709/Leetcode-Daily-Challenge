"""
Approach:
    We maintain a stack to keep track of the characters in the string.
    We iterate through the string and if the character is a digit, we pop the last character from the stack.
    If the character is a letter, we append it to the stack.
    Finally, we join the characters in the stack to form the resulting string.
Time complexity:
    O(n) where n is the length of the string.

Space complexity:
    O(n) for the stack to store the characters.
"""


def clearDigits(s: str) -> str:
    stack = []
    for i   in s:
        if i >= 'a' and i <= 'z':
            stack.append(i)
        else:
            stack.pop()
    return "".join(stack)



print(clearDigits("fs5os1os2bs3as4rs5")) #foobar