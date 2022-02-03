class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1=defaultdict(int)
        for i in nums1:
            for j in nums2:
                d1[i+j]+=1
        ans=0
        for i in nums3:
            for j in nums4:
                ans+=d1[-i-j]
        return ans