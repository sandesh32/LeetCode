class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans=0
        for i in num1:
            res=0
            rem=0
            z=1
            for j in num2[::-1]:
                temp=int(i)*int(j)+rem
                r=temp//10
                rem=r
                res=(temp%10)*z+res
                z*=10
            res=rem*z+res
            ans=ans*10+res
        return str(ans)