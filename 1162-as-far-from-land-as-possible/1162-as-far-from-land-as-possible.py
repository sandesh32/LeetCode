class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==1:
                    queue.append([i,j])
                    
        if len(queue)==n*n or len(queue)==0:
            return -1
        
        count = 0
        while len(queue)>0:
            r = len(queue)
            for p in range(r):
                temp = [[0,-1],[0,1],[-1,0],[1,0]]
                for i in temp:
                    x = queue[p][0]+i[0]
                    y = queue[p][1]+i[1]
                    if x>=0 and y>=0 and x<n and y<n and grid[x][y]==0:
                        queue.append([x,y])
                        grid[x][y]=1
            for i in range(r):
                queue.popleft()
            count+=1
            
        return count-1    