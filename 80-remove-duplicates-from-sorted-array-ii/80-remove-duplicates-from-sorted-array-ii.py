class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        previous=2
        for i in range(2,len(nums)):
            if nums[i]>nums[previous-2]:
                nums[previous]=nums[i]
                previous+=1
        return previous
                

