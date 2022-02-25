class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=list(map(int,version1.split(".")))
        v2=list(map(int,version2.split(".")))
        n=max(len(v1),len(v2))
        for i in range(n):
            if i<len(v1):
                temp1=v1[i]
            else:
                temp1=0
            if i<len(v2):
                temp2=v2[i]
            else:
                temp2=0
            if temp1>temp2:
                return 1
            elif temp1<temp2:
                return -1
        return 0
            