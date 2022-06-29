class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10**5
        tot = 0
        for num in nums:
            tot+=num
            ans = max(ans,tot)
            if tot<0:
                tot = 0
        return ans