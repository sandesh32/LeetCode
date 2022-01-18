class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        return math.factorial(m+n-2)//(math.factorial(m-1)*math.factorial(n-1))