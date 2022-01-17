# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root==None:
            return
        if root.left==None:
            self.flatten(root.right)
            return
        temp=root.right
        root.right=root.left
        root.left=None
        self.flatten(root.right)
        temp2=root
        while temp2.right:
            temp2=temp2.right
        temp2.right=temp
        self.flatten(temp)
        return