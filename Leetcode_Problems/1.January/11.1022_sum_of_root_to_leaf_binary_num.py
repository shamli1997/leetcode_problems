from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode],sum=0) -> int:
        if not root:
            return 0

        sum = sum * 2 + root.val
        if root.left or root.right:
            left_sum = self.sumRootToLeaf(root.left,sum)
            right_sum = self.sumRootToLeaf(root.right,sum)
            return left_sum + right_sum
        else:
            return sum