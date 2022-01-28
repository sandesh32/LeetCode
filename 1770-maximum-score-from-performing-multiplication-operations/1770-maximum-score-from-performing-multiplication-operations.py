class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(3000)
        def find(index,left,right):
            if index>=len(multipliers):
                return 0
            rec1=find(index+1,left+1,right)+multipliers[index]*nums[left]
            rec2=find(index+1,left,right-1)+multipliers[index]*nums[right]
            return max(rec1,rec2)
        return find(0,0,len(nums)-1)