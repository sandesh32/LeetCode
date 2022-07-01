class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = -1
        
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                if p!=-1: return False
                p = i
        return p in [-1, 0, len(nums)-2] or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]