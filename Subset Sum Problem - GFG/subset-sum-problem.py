#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, summ):
        memo={}
        def helper(i,total):
            if (i,total) in memo: return memo[(i,total)]
            if total==0: return True
            if i>=N or total<0: return False
            ans = helper(i+1,total-arr[i]) or helper(i+1,total)
            memo[(i,total)] = ans
            return ans
        return helper(0,summ)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends