class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True
        if len(t)==0: return False
        index=0
        for char in t:
            if index<len(s) and s[index]==char:
                if index>=len(s)-1:
                    return True
                index+=1
        return False