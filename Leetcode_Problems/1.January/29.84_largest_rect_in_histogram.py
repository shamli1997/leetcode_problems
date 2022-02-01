from typing import List
class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        height.append(0)
        print("height: ",height)
        stack = [-1]
        print(stack)
        ans = 0
        for i in range(len(height)):
            
            print(f"height[{i}]: {height[i]} ,height[{stack[-1]}] : {height[stack[-1]]}")
            while height[i] < height[stack[-1]]:
                print(f"stack: {stack}")
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
                print(f"ans: {ans}")
            stack.append(i)
        height.pop()
        return ans

s = Solution()
height = [2,1,5,6,2,3]
s.largestRectangleArea(height)