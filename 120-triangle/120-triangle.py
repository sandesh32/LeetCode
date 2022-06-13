class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        d=[['a' for j in range(len(triangle[i]))] for i in range(len(triangle))]
        def helper(i,j):
            if i==len(triangle):
                return 0
            if d[i][j]!='a':
                return d[i][j]
            ans = min(helper(i+1,j),helper(i+1,j+1))+triangle[i][j]
            d[i][j]=ans
            return ans
        return helper(0,0)