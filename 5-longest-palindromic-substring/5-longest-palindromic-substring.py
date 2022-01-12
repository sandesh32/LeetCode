class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        max_pal=""
        dp=[[0]*n for _ in range(n)]
        for _ in range(n):
            dp[_][_]=True
            max_pal=s[_]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    if j-i==1 or dp[i+1][j-1]==True:
                        dp[i][j]=True
                        if len(max_pal)<len(s[i:j+1]):
                            max_pal=s[i:j+1]
        return max_pal