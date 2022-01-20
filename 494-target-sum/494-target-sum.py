class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        def find(index,acc):
            if (index,acc) in self.d:
                return self.d[(index,acc)]
            if index>=len(nums):
                if acc==target:
                    return 1
                return 0
            pos = find(index+1,acc+nums[index])
            neg = find(index+1,acc-nums[index])
            self.d[(index,acc)]= pos+neg
            return self.d[(index,acc)]
        
        self.d={}
        return find(0,0)
        