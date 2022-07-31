# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return -1
            ans1 = 1 + helper(node.left)
            ans2 = 1 + helper(node.right)
            ans = max(ans1 + ans2, ans)
            return max(ans1, ans2)
        helper(root)
        return ans
            
            
        
        
        