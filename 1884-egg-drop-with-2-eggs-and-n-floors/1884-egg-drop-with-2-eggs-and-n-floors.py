class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil(((1+8*n)**0.5-1)/2)