class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        d=d.most_common(k)
        arr=[]
        for i in d:
            arr.append(i[0])
        return arr