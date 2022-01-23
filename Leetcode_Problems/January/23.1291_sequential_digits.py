from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        nl = len(str(low))# no. of digits in lower bound
        nh = len(str(high))# no. of digits in higher bound
# i is the outer window and then we will have inner loop for substring and it will be shifting
        for i in range(nl,nh + 1):
# starting point as we start from 1st digit lets say 1234 and go up till 10 - i
# why till 10 - i because let say length is 3. We are looking for 3 digit no so in start it will pick 123
# and shift it 234 till 789. 
# So our starting point will be from 0 to 6. What is this 6 is nothing but 10 - 4, but we have strictly 10 - i
# it will go till 10 - 3. So, it will go till 6 only not 7
            for j in range(0, 10 - i):
                num = int(digits[j:j+i])
                if num >= low and num <= high: result.append(num)
        return result