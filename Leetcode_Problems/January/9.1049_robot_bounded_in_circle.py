class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
#         move up towards north
        direction = (0,1)
#     starting point
        x,y = 0,0
        
        for instruction in instructions:
#             Move towards north i.e add y
            if instruction == "G":
                x,y = x + direction[0],y + direction[1]
#             change the direction for Left
            elif instruction == "L":
                direction = (-direction[1],direction[0])
#             change the direction for Right
            else:
                direction = (direction[1],-direction[0])
#         d(0,1): No circle found, Moving straight indefinitely        
        return (x==0 and y == 0) or direction != (0,1) 

s = Solution()
print(s.isRobotBounded("GGLLGG"))