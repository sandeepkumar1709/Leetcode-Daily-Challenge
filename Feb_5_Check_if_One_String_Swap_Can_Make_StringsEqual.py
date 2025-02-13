def areAlmostEqual(s1: str, s2: str) -> bool:
    s1_s, s2_s = sorted(s1), sorted(s2)
    if len(s1) != len(s2) or s1_s != s2_s:
        return False
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
        if count == 3:
            return False
    return True       
        

print(areAlmostEqual("bank", "kanb")) # True