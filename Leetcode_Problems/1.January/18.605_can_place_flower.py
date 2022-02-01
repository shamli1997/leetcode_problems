from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0 
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] ==0 and flowerbed[i-1] !=1 and flowerbed[i+1] !=1:
                count+=1
                flowerbed[i] =1
                
        return count>=n

s = Solution()
flower = [1,0,0,0,1]
n  = 1
print(s.canPlaceFlowers(flower, n))
n  = 2
print(s.canPlaceFlowers(flower, n))