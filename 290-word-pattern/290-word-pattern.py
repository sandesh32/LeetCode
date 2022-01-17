class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(s)!=len(pattern):
            return False
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]]=pattern[i]
            elif d1[s[i]]!=pattern[i]:
                return False
            if pattern[i] not in d2:
                d2[pattern[i]]=s[i]
            elif d2[pattern[i]]!=s[i]:
                return False
        return True
                