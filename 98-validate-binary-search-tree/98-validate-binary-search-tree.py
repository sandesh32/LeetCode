# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, node: Optional[TreeNode]) -> bool:
        def check(root,small,great):
            if not root:
                return True
            if root.val<=small or root.val>=great:
                return False
            return check(root.left,small,root.val) and check(root.right,root.val,great)
        
        return check(node,-10**10,10**10)
    