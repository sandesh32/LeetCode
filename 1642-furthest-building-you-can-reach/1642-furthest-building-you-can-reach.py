from queue import PriorityQueue
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = PriorityQueue()
        for i in range(len(heights)-1):
            d = heights[i+1]-heights[i]
            if d>0:
                pq.put(d)
            if pq.qsize()>ladders:
                bricks-=pq.get()
            if bricks<0:
                return i
        return len(heights)-1