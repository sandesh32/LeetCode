class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        for i in time:
            if i%60 in d:
                d[i%60]+=1
            else:
                d[i%60]=1
        count=0
        if 0 in d:
            count+=(d[0]*(d[0]-1)//2)
            d.pop(0)
        if 30 in d:
            count+=(d[30]*(d[30]-1)//2)
            d.pop(30)
        count2=0
        for i in d:
            if 60-i in d:
                count2+=(d[i]*d[60-i])
        count+=count2//2
        return count