class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp=defaultdict(int)
        ans = 0
        for i in words:
            for j in range(len(i)):
                p = i[0:j]+i[j+1:]
                dp[i]=max(dp[i],dp[p]+1)
            ans = max(ans,dp[i])
        return ans