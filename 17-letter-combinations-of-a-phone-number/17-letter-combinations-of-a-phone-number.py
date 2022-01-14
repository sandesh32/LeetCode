class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        arr=[list("abc"),list("def"),list("ghi"),list("jkl"),list("mno"),list("pqrs"),list("tuv"),list("wxyz")]
        ans=[""]
        for i in digits:
            r=int(i)
            temp=[]
            for i in arr[r-2]:
                for j in ans:
                    temp.append(j+i)
            ans=temp
        return ans