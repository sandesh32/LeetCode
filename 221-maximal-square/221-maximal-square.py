class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        ans=0
        for i in range(len(dp)):
            dp[i][0]=int(matrix[i][0])
            if dp[i][0]==1:
                ans=1
        for j in range(len(dp[0])):
            dp[0][j]=int(int(matrix[0][j]))
            if dp[0][j]==1:
                ans=1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i][j]=='1':
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans=max(ans,dp[i][j])
        return ans*ans
        
        