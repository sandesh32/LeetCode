class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d={}
        for i in s1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d2={}
        for i in range(len(s2)):
            if s2[i] in d2:
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
            if i>=len(s1)-1:
                if d==d2:
                    return True
                d2[s2[i-len(s1)+1]]-=1
                if d2[s2[i-len(s1)+1]]<=0:
                    d2.pop(s2[i-len(s1)+1])
        return False