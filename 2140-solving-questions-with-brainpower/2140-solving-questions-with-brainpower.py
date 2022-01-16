class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[i[0] for i in questions]
        for i in range(len(questions)-1,-1,-1):
            if i+questions[i][1]+1<len(questions):
                dp[i]=max(dp[i+questions[i][1]+1]+dp[i],dp[i+1])
            elif i+1<len(questions):
                dp[i]=max(dp[i],dp[i+1])
        return dp[0]