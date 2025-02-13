def clearDigits(s: str) -> str:
    letter_index = []
    i=0
    while i < (len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            letter_index.append(i)
            i+=1
        else:
            s = s[:i] + s[i+1:]
            if len(letter_index) > 0:
                latest_index = letter_index.pop()
                s = s[:latest_index] + s[latest_index+1:]
                i-=1
        
    return s



print(clearDigits("fs5os1os2bs3as4rs5")) #foobar