class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n != 1:
            temp = 0
            while n > 0:
                r = n%10
                temp = temp + r**2
                n = n // 10
            n = temp
            if temp in d:
                return False
            d[temp] = 1
        return True
            
        