class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split(".")))
        v2=list(map(int,version2.split(".")))
        while len(v1)>0 and v1[-1]==0:
            v1.pop()
        while len(v2)>0 and v2[-1]==0:
            v2.pop()
        n=min(len(v1),len(v2))
        for i in range(n):
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
        if len(v1)>len(v2):
            return 1
        elif len(v1)<len(v2):
            return -1
        return 0
            