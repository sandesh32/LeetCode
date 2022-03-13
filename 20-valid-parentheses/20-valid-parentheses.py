class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            elif len(stack)==0:
                return False
            elif i=="]" and stack[-1]=="[":
                stack.pop()
            elif i=="}" and stack[-1]=="{":
                stack.pop()
            elif i==")" and stack[-1]=="(":
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False