def removeOccurrences(s: str, part: str) -> str:
    while len(s) > 0 and part in s:
        s = s.replace(part,"",1)
    return s
print(removeOccurrences("daabcbaabcbc","abc")) #dab