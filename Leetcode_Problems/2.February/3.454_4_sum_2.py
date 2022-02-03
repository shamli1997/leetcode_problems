from typing import List
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        l1={}

        for i in nums1:
            for j in nums2:
                s=i+j
                if s not in l1:
                    l1[s]=1
                else:
                    l1[s]=l1[s]+1

        l2={}

        for i in nums3:
            for j in nums4:
                s=i+j
                if s not in l2:
                    l2[s]=1
                else:
                    l2[s]=l2[s]+1

        ans=0
        print(l1)
        print(l2)
        for i in l1.keys():
            if -i in l2.keys():
                ans=ans+l1[i]*l2[-i]

        return ans

s = Solution()
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(s.fourSumCount(nums1,nums2,nums3,nums4))