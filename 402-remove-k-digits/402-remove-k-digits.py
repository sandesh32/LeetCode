class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while k>0 and len(stack)>0 and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        if k>0:
            stack=stack[:-k]
        return "".join(stack).lstrip('0') or '0'