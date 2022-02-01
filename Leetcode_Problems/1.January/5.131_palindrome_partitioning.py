from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(curr_str, curr_path):
            if not curr_str:
                self.result.append(curr_path)
                return
            for i in range(1, len(curr_str)+1):
                if curr_str[:i] == curr_str[:i][::-1]:
                    dfs(curr_str[i:], curr_path+[curr_str[:i]])
            
        self.result = []
        dfs(s, [])
        return self.result

s = Solution()
str="aab"
result=s.partition(str)
print(result)