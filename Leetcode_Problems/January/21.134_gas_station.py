class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        shortage = 0
        
        for index in range(len(gas)):
#             fill the tank
            tank += gas[index]
#               go on to the next gas station with current gas in tank
            if tank >= cost[index]:
                tank -= cost[index]
            else:
#               we do not have enough gas to move to next station
                shortage += cost[index] - tank
#               start with the next station
                start = index + 1
#               reset the tank value
                tank = 0
# start == len(gas) then single trip is not finished if tank<shortage we won't be able to move forward
        if start == len(gas) or tank < shortage:
            return -1
        return start