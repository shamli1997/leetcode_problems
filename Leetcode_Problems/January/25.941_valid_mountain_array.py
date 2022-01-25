from typing import List
class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        N = len(a)
        i = 0
        
        # walk up
        while i+1 < N and a[i] < a[i+1]: i += 1
        #it should not be first or last
        if i == 0 or i == N - 1: return False
        # walk down
        while i+1 < N and a[i] > a[i+1]:
            i += 1
        
        return i == N-1