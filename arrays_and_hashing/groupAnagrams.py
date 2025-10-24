from collections import defaultdict
def groupAnagrams(strs):
    res=defaultdict(list)
    for s in strs:
        count=[0]*26
        for c in s:
            count[ord(c)-ord('a')]+=1
        res[tuple(count)].append(s)
    return res.values()
strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))


# Other method 
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())