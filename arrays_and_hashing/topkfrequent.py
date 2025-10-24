from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        top_k_elements = heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
        return top_k_elements
nums= [1,1,1,2,2,3]
k = 2
s=Solution()
print(s.topKFrequent(nums,k))

