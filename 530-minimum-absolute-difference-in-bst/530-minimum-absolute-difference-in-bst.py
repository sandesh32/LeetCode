# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            nonlocal diff
            nonlocal temp
            if not node:
                return 
            traverse(node.left)
            diff=min(abs(temp-node.val),diff)
            temp=node.val
            traverse(node.right)
            return
        
        temp=10**5
        diff=10**5
        traverse(root)
        return diff