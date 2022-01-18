class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        check=True
        for i in range(len(obstacleGrid[0])):
            if check==False:
                obstacleGrid[0][i]=1
                continue
            if obstacleGrid[0][i]<=0:
                obstacleGrid[0][i]=-1
            else:
                check=False
        check=True
        for i in range(len(obstacleGrid)):
            if check==False:
                obstacleGrid[i][0]=1
                continue
            if obstacleGrid[i][0]<=0:
                obstacleGrid[i][0]=-1
            else:
                check=False
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    if obstacleGrid[i-1][j]<0:
                        obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                    if obstacleGrid[i][j-1]<0:
                        obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        #print(obstacleGrid)
        if obstacleGrid[-1][-1]==1:
            return 0
        return (-1)*obstacleGrid[-1][-1]