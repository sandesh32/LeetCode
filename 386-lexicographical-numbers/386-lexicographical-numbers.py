class TrieNode:
    def __init__(self):
        self.children = {}
        
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        root = TrieNode()
        for num in range(1,n+1):
            temp = root
            num = str(num)
            for c in num:
                if c not in temp.children:
                    temp.children[c]=TrieNode()
                temp = temp.children[c]
        
        def dfs(node,val):
            if not node:
                return
            for i in node.children:
                ans.append(int(val+i))
                dfs(node.children[i],val+i)
            return
        
        dfs(root,"")
        return ans