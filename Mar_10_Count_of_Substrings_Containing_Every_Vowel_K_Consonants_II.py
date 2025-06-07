"""
Approach: 
    To count the number of substrings that contain every vowel and exactly k consonants, we can use a sliding window approach.
    We maintain a counter for the vowels and a count of consonants. We expand the right end of the window until we have all vowels and exactly k consonants, 
    then we count the valid substrings that can be formed with the current 
    left pointer(i.e. with left pointer fixed, we can move the right pointer to count all valid substrings, this can be done by maintaining a right_cons array that tells us the next index where we can find a consonant)
    then we move the left pointer to shrink the window until we no longer have k consonants or all vowels.
Time Complexity:
    O(n) where n is the length of the word. We iterate through the word once or at max twice.
Space Complexity:
    O(n) since we are maintaining the index of the next consonant for each index in the word.
"""

def countOfSubstrings(word: str, k: int) -> int:
    def status():
        return len(counter) == 5
        # for ele in counter:
        #     if counter[ele] == 0:
        #         return False
        # return True

    counter,cons,ans,left = {},0,0,0
    right_cons = [-1] * len(word)
    cons = len(word)
    for i in range(len(word)-1,-1,-1):
        right_cons[i] = cons
        if word[i] not in 'aeiou':
            cons = i
        

    # print(right_cons)
    cons = 0
    for right in range(len(word)):
        if word[right] in "aeiou":
            counter[word[right]] = counter.get(word[right],0)+1
        else:
            cons+=1
        # print(counter, cons, status())
        while status() and cons == k:
            # print("reacched here, ", right)
            ans += right_cons[right] - right
            if word[left] in "aeiou":
                counter[word[left]]-=1
                if counter[word[left]] == 0:
                    del counter[word[left]]
            else:
                cons-=1
            left+=1
        while cons > k:
            if word[left] in "aeiou":
                counter[word[left]]-=1
                if counter[word[left]] == 0:
                    del counter[word[left]]
            else:
                cons-=1
            left += 1


    return ans
    
print(countOfSubstrings("aeiouaeiou", 2))  # expected 0
print(countOfSubstrings("aoaiuefi", 1))  # expected 4