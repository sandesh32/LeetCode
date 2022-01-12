# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        def bst(root,val):
            if val>=root.val:
                if root.right!=None:
                    bst(root.right,val)
                else:
                    root.right=TreeNode(val)
                    return
            else:
                if root.left!=None:
                    bst(root.left,val)
                else:
                    root.left=TreeNode(val)
                    return
        
        bst(root,val)
        return root