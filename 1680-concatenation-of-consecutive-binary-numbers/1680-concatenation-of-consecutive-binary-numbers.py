class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result=0
        for i in range(n):
            result=(result*(1<<(len(bin(i+1))-2))+i+1)%(10**9+7)
        return result