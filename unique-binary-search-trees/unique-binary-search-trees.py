class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return 1
        arr=[0 for i in range(n+1)]
        arr[1]=1
        arr[2]=2
        for i in range(3,n+1):
            arr[i]+=2*arr[i-1]
            for j in range(2,i):
                arr[i]+=(arr[i-j]*arr[i-1-(i-j)])
        return arr[-1]
                