class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=bin(n)[2:]
        l=len(a)-1
        ans=0
        for i in a:
            ans+=(2**l)*((int(i)+1)%2)
            l-=1
        return ans
