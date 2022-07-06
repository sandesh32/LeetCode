class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n):
            temp = a
            a = a + b
            b = temp
        return a