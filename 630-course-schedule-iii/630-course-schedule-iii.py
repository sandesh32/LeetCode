class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        pass_time = 0
        heap = []
        for i in courses:
            pass_time+=i[0]
            heapq.heappush(heap,-i[0])
            while pass_time>i[1]:
                pass_time+=heapq.heappop(heap)
        return len(heap)