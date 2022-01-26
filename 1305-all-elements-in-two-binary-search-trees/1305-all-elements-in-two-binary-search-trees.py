# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
            
        def getElements(root,arr):
            if not root:
                return []
            getElements(root.left,arr)
            arr.append(root.val)
            getElements(root.right,arr)
            return arr
        
        arr1=getElements(root1,[])
        arr2=getElements(root2,[])
        if len(arr1)==0:
            return arr2
        if len(arr2)==0:
            return arr1
        
        # 1 2 3 0 0 0
        # 4 5 6
        ptr1=len(arr1)-1
        ptr2=len(arr2)-1
        for i in range(len(arr2)):
            arr1.append(0)
        while ptr1>=0 and ptr2>=0:
            if arr1[ptr1]>=arr2[ptr2]:
                arr1[ptr1+ptr2+1]=arr1[ptr1]
                ptr1-=1
            else:
                arr1[ptr1+ptr2+1]=arr2[ptr2]
                ptr2-=1
        while ptr2>=0:
            arr1[ptr2]=arr2[ptr2]
            ptr2-=1
        return arr1        