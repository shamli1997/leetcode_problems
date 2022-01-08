from typing import List
from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return 0
            # current cell
            result = 0
            result += grid[row][col1]
            print(f"result:grid[{row}][{col1}]: {result}")
            if col1 != col2:
                result += grid[row][col2]
                print(f"col1 != col2: result:grid[{row}][{col1}]: {result}")
            # transition
            if row != m-1:
                print("TRANSITION:")
                maximum = max(dp(row+1, new_col1, new_col2)
                              for new_col1 in [col1, col1+1, col1-1]
                              for new_col2 in [col2, col2+1, col2-1])
                result += maximum
                print(f"Max:{maximum}")
                print(f"row != m - 1: result {result}")
            print(f"Returning {result}")
            return result
        print(f"Calling dp(0,0 n-1)")
        return dp(0, 0, n-1)
        
s = Solution()
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(s.cherryPickup(grid))