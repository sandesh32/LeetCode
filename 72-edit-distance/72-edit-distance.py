class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d={}
        def helper(i,j):
            if i==len(word1) and j==len(word2):
                return 0
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if (i,j) not in d:
                if word1[i]==word2[j]:
                    ans = helper(i+1,j+1)
                else:
                    insert = 1 + helper(i,j+1)
                    delete = 1 + helper(i+1,j)
                    replace = 1 + helper(i+1,j+1)
                    ans = min(insert,delete,replace)
                d[(i,j)] = ans
            return d[(i,j)]
        return helper(0,0)