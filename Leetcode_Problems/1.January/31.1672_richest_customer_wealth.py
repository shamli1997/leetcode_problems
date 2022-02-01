from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for a in accounts:
            wealth = sum(a)
            maxWealth = max(maxWealth, wealth)
        return maxWealth