def isValidPallindrom(s):
    l=0
    r=len(s)-1
    while(l<r):
        while l<r and not s[l].isalnum():
            l+=1
        while l<r and not s[r].isalnum():
            r-=1
        if s[l].lower()!=s[r].lower():
            return False
    return True
s="A man, a plan, a canal: Panama"
print(isValidPallindrom(s))
   
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return string == string[::-1]



