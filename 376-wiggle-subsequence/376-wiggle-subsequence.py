class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1: return len(nums)
        dp = [[0,0] for i in range(len(nums))]
        dp[-1] = [1,1]
        ans = 1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    dp[i][0] = max(dp[i][0],dp[j][1]+1)
                if nums[i]<nums[j]:
                    dp[i][1] = max(dp[i][1],dp[j][0]+1)
            ans = max(ans,dp[i][0],dp[i][1])
        return ans