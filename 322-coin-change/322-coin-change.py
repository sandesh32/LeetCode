class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10**4+1 for i in range(amount+1)]
        dp[0] = 0
        coins.sort()
        for i in range(len(coins)):
            for j in range(len(dp)):
                if j - coins[i] >= 0:
                    if dp[j-coins[i]] < 10**4:
                        dp[j] = min(dp[j-coins[i]] + 1, dp[j])
        if dp[-1] > 10**4:
            dp[-1] = -1
        return dp[-1]