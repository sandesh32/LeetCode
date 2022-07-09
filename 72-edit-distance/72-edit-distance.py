class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = [[-1 for i in range(len(word2))] for j in range(len(word1))]
        def helper(i,j):
            if i >= len(word1) and j>=len(word2):
                return 0
            if i >= len(word1):
                return len(word2)- j
            if j >= len(word2):
                return len(word1) - i
            if d[i][j] != -1:
                return d[i][j]
            else:
                if word1[i] == word2[j]:
                    ans = helper(i+1,j+1)
                else:
                    ans1 = 1 + helper(i + 1,j)
                    ans2 = 1 + helper(i + 1, j + 1)
                    ans3 = 1 + helper(i, j + 1)
                    ans = min(ans1, ans2, ans3)
                d[i][j] = ans
                return ans
                    
        return helper(0,0)