#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        dp = [0]*(n+3)
        dp[1]=1
        dp[2]=2
        dp[3]=4
        for i in range(4,len(dp)):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007
        return dp[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends