class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            d[s[i]]=i
        t1=0
        t2=0
        res=[]
        for i in range(len(s)):
            t1=max(t1,d[s[i]])
            if t1==i:
                res.append(i-t2+1)
                t2=i+1
        return res