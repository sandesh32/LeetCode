class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        
        ans = [[10**5 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0: ans[i][j]=0
                if i>0: ans[i][j]=min(ans[i][j],ans[i-1][j]+1)
                if j>0: ans[i][j]=min(ans[i][j],ans[i][j-1]+1)
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i<n-1: ans[i][j]=min(ans[i][j],ans[i+1][j]+1)
                if j<m-1: ans[i][j]=min(ans[i][j],ans[i][j+1]+1)
                
        return ans            