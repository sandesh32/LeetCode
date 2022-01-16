class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1,i+nums[i]+1):
                try:
                    dp[j]=min(dp[i]+1,dp[j])
                except:
                    pass
        print(dp[:len(nums)])
        return dp[-1]