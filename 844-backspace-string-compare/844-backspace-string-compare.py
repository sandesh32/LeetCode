class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stakc = []
        for i in s:
            if i=="#":
                try:
                    stack.pop()
                except:
                    pass
            else:
                stack.append(i)
        for i in t:
            if i=="#":
                try:
                    stakc.pop()
                except:
                    pass
            else:
                stakc.append(i)
        return stack == stakc