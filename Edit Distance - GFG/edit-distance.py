class Solution:
	def editDistance(self, s, t):
	    d={}
	    def helper(i,j):
	        if (i,j) in d:
	            return d[(i,j)]
	        elif i==len(s) and j==len(t):
	            ans = 0
	        elif i==len(s):
	            ans = len(t)-j
	        elif j==len(t):
	            ans = len(s)-i
	        elif s[i]==t[j]:
	            ans = helper(i+1,j+1)
	        else:
	            insert = 1 + helper(i,j+1)
	            remove = 1 + helper(i+1,j)
	            replace = 1 + helper(i+1,j+1)
	            ans = min(insert, remove, replace)
	        d[(i,j)]=ans
	        return ans
        return helper(0,0)
	            
	            

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends