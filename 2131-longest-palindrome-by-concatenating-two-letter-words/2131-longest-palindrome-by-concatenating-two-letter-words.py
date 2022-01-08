class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        check=True
        for i in d:
            if i==i[::-1]:
                if i in d:
                    if d[i]%2==0:
                        count+=2*d[i]
                    else:
                        if check==True:
                            count+=2*d[i]
                            check=False
                        else:
                            count+=2*(d[i]-1)
            elif i[::-1] in d:
                count+=2*min(d[i],d[i[::-1]])
        return count
                
            
            