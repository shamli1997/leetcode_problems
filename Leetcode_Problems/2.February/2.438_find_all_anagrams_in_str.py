import collections
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0 
        dic_pattern = collections.Counter(p)
        dic_s = {}
        result = []
        
        for end in range(len(s)):
            if s[end] not in dic_s:
                dic_s[s[end]] = 1
            else:
                dic_s[s[end]] += 1
            
            if dic_s == dic_pattern:
                result.append(start)
                
            if (end - start +1) >= len(p): 
                if dic_s[s[start]] > 1:
                    dic_s[s[start]] -= 1
                else:
                    del dic_s[s[start]]
                start += 1
        return result