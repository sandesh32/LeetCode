class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count=1
        present=points[0][1]
        for i in points:
            if i[0]<=present and i[1]>=present:
                continue
            count+=1
            present=i[1]
        return count