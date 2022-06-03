class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==len(text1) or j==len(text2):
                ans = 0
            elif text1[i]==text2[j]:
                ans = 1 + helper(i+1,j+1)
            else:
                ans = max(helper(i+1,j),helper(i,j+1))
            memo[(i,j)] = ans
            return ans
        return helper(0,0)