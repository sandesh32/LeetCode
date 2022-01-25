# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(left,right):
            if left>right:
                return [None]
            ans=[]
            for root in range(left,right+1):
                for x in helper(left,root-1):
                    for y in helper(root+1,right):
                        node=TreeNode(root)
                        node.left=x
                        node.right=y
                        ans.append(node)
            return ans
        
        return helper(1,n)