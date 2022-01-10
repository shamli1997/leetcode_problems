class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len, b_len = -len(a), -len(b)
        i, carry, result = -1, 0, ""

        while i >= a_len or i >= b_len:
            a_bit = int(a[i]) if i >= a_len else 0 #if len of a<b then take 0 for addition
            b_bit = int(b[i]) if i >= b_len else 0 #if len of b<a then take 0 for addition

            sum = a_bit + b_bit + carry
            result = str(sum % 2) + result
            carry = sum // 2
            i -= 1

        return "1" + result if carry else result

s = Solution()
print(s.addBinary("1101","1111"))