class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums2 = nums[::-1]
        for i in range(1,len(nums)):
            nums[i] *= nums[i-1] or 1
            nums2[i] *= nums2[i-1] or 1
        return max(nums+nums2)