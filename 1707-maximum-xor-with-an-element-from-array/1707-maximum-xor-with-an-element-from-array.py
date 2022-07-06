class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def insert(self, num):
        children = self.children
        for i in range(31,-1,-1):
            r = (num >> i) & 1
            if r not in children:
                children[r] = {}
            children = children[r]
    
    def query(self, num):
        if not self.children: return -1
        children = self.children
        ans = 0
        for i in range(31, -1, -1):
            r = (num >> i) & 1
            if 1 - r in children:
                ans += 2 ** i
                children = children[1 - r]
            else:
                children = children[r]
        return ans 
        
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        queries = sorted(enumerate(queries), key = lambda x: x[1][1])
        nums.sort()
        trie = TrieNode()
        ans = [0 for i in range(len(queries))]
        ptr = 0
        for query in queries:
            while ptr < len(nums) and nums[ptr] <= query[1][1]:
                trie.insert(nums[ptr])
                ptr += 1
            ans[query[0]] = trie.query(query[1][0])
        return ans
