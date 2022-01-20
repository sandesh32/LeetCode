class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def find(s1,pos):
            if (s1,pos) in d2:
                return d2[(s1,pos)]
            if s1 in d1:
                return True
            if pos==1:
                return False
            ans=False
            for i in range(1,len(s1)):
                ans = ans or (find(s1[i:],0) and find(s1[0:i],1))
                if ans==True:
                    d2[(s1,pos)]=True
                    return True
            d2[(s1,pos)]=False
            return ans
        d1={i:1 for i in wordDict}
        d2={}
        return find(s,0)
