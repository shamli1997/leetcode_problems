from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         If root is empty then make the new Node with given val and return
        if root == None:
            return TreeNode(val)
        curr = root
        while True:
#             Traverse to the left most node and insert
            if val <= curr.val:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
#             Traverse to the right most node and insert
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
                
        return root
            
                
        