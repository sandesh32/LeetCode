#User function Template for python3

class Solution:
	def longestIncreasingPath(self, matrix):
		dp=[]
		for i in range(len(matrix)):
		    temp=[]
		    for j in range(len(matrix[0])):
		        temp.append(0)
		    dp.append(temp)
		def helper(x,y):
		    if dp[x][y]: return dp[x][y]
		    ans = 1
		    if x-1>=0 and matrix[x-1][y]>matrix[x][y]:
		        ans = max(ans, 1 + helper(x-1,y))
		    if x+1<len(matrix) and matrix[x+1][y]>matrix[x][y]:
		        ans = max(ans, 1 + helper(x+1,y))
		    if y-1>=0 and matrix[x][y-1]>matrix[x][y]:
		        ans = max(ans, 1 + helper(x,y-1))
		    if y+1<len(matrix[0]) and matrix[x][y+1]>matrix[x][y]:
		        ans = max(ans, 1 + helper(x,y+1))
		    dp[x][y] = ans
		    return ans
		        
		res = 1
		for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
		        if dp[i][j]:
		            res = max(res,dp[i][j])
		        else:
		            res = max(res,helper(i,j))
		return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.longestIncreasingPath(matrix)
		print(ans)

# } Driver Code Ends