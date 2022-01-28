class Solution:
    def findMaximumXOR(self, arr: List[int]) -> int:
        maxx = 0
        mask = 0;
        n=len(arr)
        se = set()
        for i in range(30, -1, -1):
            mask |= (1 << i)
            newMaxx = maxx | (1 << i)
            for i in range(n):
                se.add(arr[i] & mask)
            for prefix in se:
                if (newMaxx ^ prefix) in se:
                    maxx = newMaxx
                    break
            se.clear()
        return maxx