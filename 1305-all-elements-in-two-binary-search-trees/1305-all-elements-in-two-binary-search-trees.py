# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
            
        def insertElement(root,node):
            if root==None:
                return node
            if node.val>=root.val:
                root.right = insertElement(root.right,node)
            else:
                root.left = insertElement(root.left,node)
            return root
            
        def getElements(root,arr):
            if not root:
                return
            getElements(root.left,arr)
            arr.append(root.val)
            getElements(root.right,arr)
            return arr
        
        def merge(root):
            if not root:
                return
            merge(root.left)
            merge(root.right)
            root.left=None
            root.right=None
            insertElement(root1,root)
            return
        
        if root1 is None:
            return getElements(root2,[])
        
        merge(root2)
        return getElements(root1,[])