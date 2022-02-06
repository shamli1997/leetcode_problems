from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        count = 1
        for i in range(1,len(nums)-1):
            if nums[i-1]!=nums[i+1]:
                nums[count] = nums[i]
                count += 1
        nums[count] = nums[-1]
        print(nums)
        return count + 1

s = Solution()
l1 = [1,1,2]
print(s.removeDuplicates(l1))

