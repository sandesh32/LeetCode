class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def helper(i,j):
            if i>=len(word1) or j>=len(word2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i]==word2[j]:
                ans = 1+helper(i+1,j+1)
            else:
                ans = max(helper(i+1,j),helper(i,j+1))
            dp[(i,j)] = ans
            return ans
        helper(0,0)
        return len(word1)+len(word2)-2*dp[(0,0)]
            