class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.ends = False
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        
        for word in words:
            temp = root
            for c in word[::-1]:
                if c not in temp.children:
                    temp.children[c]=TrieNode()
                temp = temp.children[c]
            temp.ends = True
        
        ans = 0
        temp = root
        
        def dfs(node,total):
            nonlocal ans
            if len(node.children)==0:
                ans+=(total+1)
                return
            for c in node.children:
                dfs(node.children[c],total+1)
            return
        
        dfs(root,0)
        return ans
            
            
        
        
                