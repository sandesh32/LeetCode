class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0 for i in range(n)] 
        for i, j in trust:
            count[i-1] -= 1
            count[j-1] += 1
        for i in range(n):
            if count[i] == n-1:
                return i+1
        return -1