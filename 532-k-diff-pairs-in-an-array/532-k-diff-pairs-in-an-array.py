class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        count=0
        if k==0:
            for i in d:
                if d[i]>1:
                    count+=1
            return count
        for i in d:
            if (i+k) in d:
                count+=1
        return count