class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        num_arrived=False
        sign=1
        for i in s:
            if i.isalpha()==True or i==".":
                break
            if num_arrived==True and i.isdigit()==False:
                break
            if i=="+" or i=="-":
                num_arrived=True
                if i=="-":
                    sign=-1
            if i.isdigit()==True:
                num_arrived=True
                ans=ans*10+int(i)
        ans*=sign
        if ans>2**31-1:
            return 2**31-1
        if ans<-2**31:
            return -2**31
        return ans