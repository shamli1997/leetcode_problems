class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while len(str(res)) > 1:
            div_num = res // 10
            rem = res % 10
            res = div_num + rem
            
        return res