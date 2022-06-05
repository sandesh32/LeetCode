#User function Template for python3


#Function to find the maximum possible amount of money we can win.

class Solution:
    def optimalStrategyOfGame(self,arr, n):
        memo = {}
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
        return helper(0,n-1)
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(arr,n))

# } Driver Code Ends