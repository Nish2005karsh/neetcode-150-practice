def validAnagram(s,t):
    ss=sorted(s)
    tt=sorted(t)
    return ss==tt
s = "anagram"
t = "nagaram"
print(validAnagram(s,t))