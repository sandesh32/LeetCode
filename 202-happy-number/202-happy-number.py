class Solution:
    def isHappy(self, n: int) -> bool:
        def findsum(n):
            temp = 0
            while n > 0:
                r = n%10
                temp = temp + r**2
                n = n // 10
            return temp
        
        b = findsum(n)
        a = n
        while True:
            if a == 1:
                return True
            if a == b:
                return False
            a = findsum(a)
            b = findsum(findsum(b))
        
            
        