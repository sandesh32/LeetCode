class Solution:
    def PredictTheWinner(self,arr: List[int]) -> bool:
        memo = {}
        n=len(arr)
        def helper(i,j):
            if i==j:
                return arr[i]
            elif j==i+1:
                ans = max(arr[i],arr[j])
                memo[(i,j)]=ans
            elif (i,j) in memo:
                return memo[(i,j)]
            elif i>j:
                return 0
            else:
                ans1 = arr[i] + min(helper(i+2,j),helper(i+1,j-1))
                ans2 = arr[j] + min(helper(i,j-2),helper(i+1,j-1))
                ans = max(ans1,ans2)
                memo[(i,j)]=ans
            return ans
        ans = helper(0,n-1)
        return ans>=sum(arr)-ans