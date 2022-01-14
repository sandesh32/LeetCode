# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def lot(root,level,arr):
            if root:
                if level>=len(arr):
                    arr.append([root.val])
                else:
                    arr[level].append(root.val) 
            else:
                return
            if root.left: lot(root.left,level+1,arr)
            if root.right: lot(root.right,level+1,arr)
            return 
        arr=[]
        lot(root,0,arr)
        return arr