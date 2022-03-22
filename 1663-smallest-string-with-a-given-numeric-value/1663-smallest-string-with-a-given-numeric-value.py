class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        num2 = (k-n)// 25
        if num2 == n: 
            return 'z' * n

        num1 = n - num2 - 1
        num = k - (num1 + num2 * 26)
        return 'a' * num1 + chr(num+96) + 'z' * num2