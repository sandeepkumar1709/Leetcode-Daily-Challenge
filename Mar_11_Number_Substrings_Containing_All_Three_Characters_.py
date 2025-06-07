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