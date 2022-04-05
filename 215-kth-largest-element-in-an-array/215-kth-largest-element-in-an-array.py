class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for i in nums:
            heapq.heappush(arr,-i)
        for i in range(k-1):
            heapq.heappop(arr)
        return heapq.heappop(arr)*(-1)