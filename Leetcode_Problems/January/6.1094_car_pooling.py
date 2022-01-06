# 1.Create capacity array of 1001 filled with 0.
# 2.Increment the capacityArray by trip when passenger onboards.
# 3.Decrement the capacityArray by trip when passenger departs.
# 4.Loop over capacityArray and decrement the passenger from given capacity.
# 5.Return false if capacity < passenger present in the capacity_array.
# Time Complexity: O(n) AND Space Complexity: o(max(n,1001)).
from typing import List
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capacity_array = [0 for i in range(1001)]
        
        for trip,i,j in trips:
            capacity_array[i] += trip #increment the passenger in capacity_array
            capacity_array[j] -= trip #decrement the passenger in capacity_array
        
        for passenger in capacity_array:
            capacity -=passenger #decrement pasenger from the given capacity
            if capacity < 0:
                return False
        return True

s = Solution()
trips=[[2,1,5],[3,3,7]]
capacity=5
print(s.carPooling(trips,capacity))
trips=[[2,1,5],[3,3,7]]
capacity=4
print(s.carPooling(trips,capacity))