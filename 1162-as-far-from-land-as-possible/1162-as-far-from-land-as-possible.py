class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        ans = [[10**5 for i in range(n)] for j in range(n)]
        
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    ans[i][j]=0
                    count+=1
                if i>0: ans[i][j]=min(ans[i][j],ans[i-1][j]+1)
                if j>0: ans[i][j]=min(ans[i][j],ans[i][j-1]+1)
        
        if count==0 or count==n*n: return -1
        
        res = 0
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i<n-1: ans[i][j]=min(ans[i][j],ans[i+1][j]+1)
                if j<n-1: ans[i][j]=min(ans[i][j],ans[i][j+1]+1)
                res = max(ans[i][j],res)
        return res
                
                
                   