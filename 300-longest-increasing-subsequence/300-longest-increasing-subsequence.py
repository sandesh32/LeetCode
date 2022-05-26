class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            maxm=0
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    maxm=max(maxm,dp[j])
            dp[i]+=maxm
        return max(dp)
                