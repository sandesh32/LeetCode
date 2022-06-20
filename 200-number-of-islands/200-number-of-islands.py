class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(i,j):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]):
                if grid[i][j]=="1":
                    grid[i][j]="0"
                    helper(i-1,j)
                    helper(i,j-1)
                    helper(i+1,j)
                    helper(i,j+1)
            return
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    ans+=1
                    helper(i,j)
        return ans