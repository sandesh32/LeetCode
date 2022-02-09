class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d=collections.Counter(nums)
        count=0
        for i in d:
            if (k>0 and (i+k) in d) or (k==0 and d[i]>1) :
                count+=1
        return count
