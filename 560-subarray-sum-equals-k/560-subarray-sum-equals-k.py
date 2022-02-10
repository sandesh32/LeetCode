class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        ans=0
        total=0
        for num in nums:
            total+=num
            if (total-k) in d:
                ans+=d[total-k]
            if total in d:
                d[total]+=1
            else:
                d[total]=1
        return ans