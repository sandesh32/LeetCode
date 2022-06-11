class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        d1={0:0}
        d2={0:0}
        ps1=0
        ps2=0
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            ps1+=nums[i]
            d1[ps1]=(i+1)
        if x>total:
            return -1
        for j in range(len(nums)-1,-1,-1):
            ps2+=nums[j]
            d2[ps2]=(len(nums)-j)
        ans = len(nums)
        check = False
        for i in d1:
            if (x-i) in d2:
                ans = min(ans,d1[i]+d2[x-i])
                check = True
        if check:
            return ans
        return -1