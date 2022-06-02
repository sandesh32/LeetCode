class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        maxHeap = [(-v,k) for k,v in d.items()]
        heapq.heapify(maxHeap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans
   