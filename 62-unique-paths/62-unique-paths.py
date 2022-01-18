class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr=[[0]*m]*n
        arr[0]=[1]*m
        for i in arr:
            i[0]=1
        for i in range(1,n):
            for j in range(1,m):
                arr[i][j]=arr[i-1][j]+arr[i][j-1]
        return arr[-1][-1]