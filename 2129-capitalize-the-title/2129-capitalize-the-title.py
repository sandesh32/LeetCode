class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr=title.split()
        ans=""
        for i in arr:
            if len(i)>2:
                ans+=i[0].upper()+i[1:].lower()+" "
            else:
                ans+=i.lower()+" "
        return ans[:-1]