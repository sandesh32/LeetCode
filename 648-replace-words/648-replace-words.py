class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d={i:1 for i in dictionary}
        ans=""
        check=True
        res=""
        for i in sentence:
            res+=i
            if check==True and res in d:
                ans+=res
                check=False
            if i==" ":
                if check:
                    ans+=res
                else:
                    check=True
                    ans+=" "
                res=""
        if check:
            ans+=res
        return ans