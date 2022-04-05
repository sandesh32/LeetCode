class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue as pq
        pq1=pq()
        for i in nums:
            pq1.put(i*(-1))
        while k>0:
            ans=pq1.get()
            k-=1
        return ans*(-1)