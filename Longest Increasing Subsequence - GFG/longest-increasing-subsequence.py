#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp = [1]*n
        dp[-1]=1
        ans = 1
        for i in range(len(a)-2,-1,-1):
            for j in range(i+1,len(a)):
                if a[i]<a[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    ans = max(dp[i],ans)
        return ans
                    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends