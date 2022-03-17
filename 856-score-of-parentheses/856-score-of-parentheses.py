class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count=0
        ans=0
        for i,char in enumerate(s):
            if char=="(":
                count+=1
            else:
                count-=1
                if s[i-1]=="(":
                    ans+=2**count                
        return ans