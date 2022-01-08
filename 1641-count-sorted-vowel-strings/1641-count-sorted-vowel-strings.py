class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==1:
            return 5
        arr=[[0]*6 for i in range(n)]
        for i in range(1,6):
            arr[0][i]=1
        for i in range(1,n):
            s=sum(arr[i-1])
            temp_sum=0
            for j in range(1,6):
                arr[i][j]=s-temp_sum
                temp_sum+=arr[i-1][j]
        return sum(arr[-1])