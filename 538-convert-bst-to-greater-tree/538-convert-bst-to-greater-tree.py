# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=0
        def calculate(node):
            nonlocal total
            if not node:
                return 
            calculate(node.right)
            total+=node.val
            node.val=total
            calculate(node.left)
            return
        calculate(root)
        return root
        