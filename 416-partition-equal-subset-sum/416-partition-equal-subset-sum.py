class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2: return False
        dp = [False for i in range(s//2 + 1)]
        dp[0] = True
        nums.sort()
        for j in nums:
            for i in range(s//2, -1, -1):
                if dp[i] == True and i + j <= s//2:
                    dp[i + j] = True
                    if i + j == s//2:
                        return True
        return dp[s//2]
    #1 1 1 1 0
                
        
        