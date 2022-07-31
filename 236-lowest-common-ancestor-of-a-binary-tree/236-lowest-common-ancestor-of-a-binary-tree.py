# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None]
        checked = [False]
        def helper(node):
            if checked[0]:
                return [False, False]
            if not node:
                return [False, False]
            p1, q1 = helper(node.left)
            p2, q2 = helper(node.right)
            if node == p:
                p1 = True
            if node == q:
                q1 = True
            if (p1|p2) and (q1|q2):
                ans[0] = node
                checked[0] = True
                return [False, False]
            else:
                return [p1|p2, q1|q2]
                
        helper(root)
        return ans[0]
            
            
            
        
            