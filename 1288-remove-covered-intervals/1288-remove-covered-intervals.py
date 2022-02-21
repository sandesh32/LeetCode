class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        res=0
        right=0
        for i in intervals:
            res += i[1] > right
            right = max(right, i[1])
        return res