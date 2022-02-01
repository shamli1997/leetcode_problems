class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 2
        while(mask<=n):
            mask*=2
        return mask-1-n

s = Solution()
print(s.bitwiseComplement(5))