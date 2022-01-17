class Solution(object):
    def wordPattern(self, pattern, s):
        dic = {}
        words = s.split(' ')
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)): return False
        for i, p in enumerate(pattern):
            if p in dic:
                if dic[p] != words[i]:
                    return False
            else:
                dic[p] = words[i]
        return True

s = Solution()
pattern = "abba"
str = "dog cat cat dog"
print(s.wordPattern(pattern,str))
str = "dog cat cat cat"
print(s.wordPattern(pattern,str))