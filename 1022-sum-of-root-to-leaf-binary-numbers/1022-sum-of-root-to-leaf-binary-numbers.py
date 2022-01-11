# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root.left==None and root.right==None:
            return root.val
        def dfs(node,arr,temp):
            if node.left==None and node.right==None:
                arr.append(temp)
                return
            if node.right!=None:
                dfs(node.right,arr,temp+[node.right.val])
            if node.left!=None:
                dfs(node.left,arr,temp+[node.left.val])
            return arr
        arr=dfs(root,[],[root.val])
        ans=0
        for i in arr:
            n=len(i)-1
            temp_ans=0
            for j in i:
                temp_ans+=j*2**n
                n-=1
            ans+=temp_ans
        return ans