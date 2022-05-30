class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: 
        def bfs(y,x):
            queue = deque()
            visited={}
            queue.append((y,x,0))
            while len(queue)>0:
                r=queue.popleft()
                y=r[0]
                x=r[1]
                d=r[2]
                if grid[y][x]==2:
                    return r[2]
                elif grid[y][x]==0:
                    continue
                if y>0 and y<len(grid) and x>=0 and x<len(grid[0]) and (y-1,x) not in visited:
                    queue.append((y-1,x,d+1))
                if y>=0 and y<len(grid) and x>0 and x<len(grid[0]) and (y,x-1) not in visited:
                    queue.append((y,x-1,d+1))
                if y>=0 and y<len(grid)-1 and x>=0 and x<len(grid[0]) and (y+1,x) not in visited:
                    queue.append((y+1,x,d+1))
                if y>=0 and y<len(grid) and x>=0 and x<len(grid[0])-1 and (y,x+1) not in visited:
                    queue.append((y,x+1,d+1))
                visited[(y,x)]=1
            return -1
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans1 = bfs(i,j)
                    if ans1==-1:
                        return -1
                    ans = max(ans,ans1)
                    
        return ans