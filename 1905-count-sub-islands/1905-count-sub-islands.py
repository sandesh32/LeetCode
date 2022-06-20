class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def helper(i,j):
            if i>=0 and j>=0 and i<len(grid2) and j<len(grid2[0]):
                if grid2[i][j]==1:
                    grid2[i][j]=0
                    helper(i-1,j)
                    helper(i,j-1)
                    helper(i+1,j)
                    helper(i,j+1)
            return
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    helper(i,j)
        
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]==1:
                    ans+=1
                    helper(i,j)
        return ans