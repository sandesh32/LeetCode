# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #for your review 1, i want your title, abstract, references
        if n==1:
            return [TreeNode(1)]
        
        def LevelOrder(root,ans):
            if root is None:
                return 
            queue=[]
            queue.append(root)
            while(len(queue) > 0):
                ans.append(queue[0].val)
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return ans
        
        def insertval(node,k):
            if node==None:
                return TreeNode(k)
            if node.val>=k:
                node.left = insertval(node.left,k)
            else:
                node.right = insertval(node.right,k)
            return node
        
        def makearray(node,k,arr=[]):
            if node==None:
                return arr
            else:
                if node.left:
                    arr.append(node.left.val)
                if node.right:
                    arr.append(node.right.val)
                makearray(node.left)
        
        arr=["1","12","123","1234","12345","123456","1234567","12345678"]
        per=list(permutations(arr[n-1],n))
        ans=[]
        dic={}
        for item in per:
            node=TreeNode(int(item[0]))
            for x in range(1,len(item)):
                insertval(node,int(item[x]))
            t1=tuple(LevelOrder(node,[]))
            if t1 not in dic:
                dic[t1]=1
                ans.append(node)
        print(len(ans))
        return ans