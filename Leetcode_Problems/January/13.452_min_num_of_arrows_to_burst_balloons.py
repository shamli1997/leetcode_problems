import math
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
#         sort the list based on 2nd element
        points.sort(key=lambda x:x[1])
        arrows = 0
        ending = -math.inf
#         check the overlapping interval
        for pair in points:
            if pair[0] > ending:
                arrows += 1 # if overlapping interval then increment the arrow
                ending = pair[1] # update the new ending
        return arrows

s = Solution()
points=[[10,16],[2,8],[1,6],[7,12]]
print(s.findMinArrowShots(points))