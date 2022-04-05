class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            return
        pivot = nums[len(nums)//2]
        left = [i for i in nums if i>pivot]
        mid = [i for i in nums if i==pivot]
        right = [i for i in nums if i<pivot]
        if k<=len(left):
            return self.findKthLargest(left,k)
        elif k>len(left)+len(mid):
            return self.findKthLargest(right,k-len(left)-len(mid))
        else:
            return mid[0]