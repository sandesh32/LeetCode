class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        
        ans = [[10**5 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    queue.append([i,j])
                    ans[i][j]=0
        
        count = 0
        while len(queue)>0:
            r = len(queue)
            count+=1
            for p in range(r):
                temp = [[0,-1],[0,1],[-1,0],[1,0]]
                for i in temp:
                    x = queue[p][0]+i[0]
                    y = queue[p][1]+i[1]
                    if x>=0 and y>=0 and x<n and y<m and grid[x][y]==1:
                        queue.append([x,y])
                        grid[x][y]=0
                        ans[x][y] = count
            for i in range(r):
                queue.popleft()
        
        return ans