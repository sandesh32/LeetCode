class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        d=sorted(d.items(), key=lambda x:x[1])
        d.reverse()
        ans = []
        for i in range(k):
            ans.append(d[i][0])
        return ans
