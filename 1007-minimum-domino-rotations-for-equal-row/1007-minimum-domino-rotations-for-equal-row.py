class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        check1 = True
        check2 = True
        for i in range(n):
            if tops[i] != tops[0] and bottoms[i] != tops[0]: check1 = False
            if tops[i] != bottoms[0] and bottoms[i] != bottoms[0]: check2 = False
            if check1 == check2 == False: return -1
        c1 = tops.count(tops[0])
        c2 = bottoms.count(tops[0])
        c3 = tops.count(bottoms[0])
        c4 = bottoms.count(bottoms[0])
        if not check1: return n - max(c3, c4)
        if not check2: return n - max(c1, c2)
        return n - max(c1, c2, c3, c4)