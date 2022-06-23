class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 1
        index = [0,1]
        for i in range(2*len(s)-1):
            ptr1 = i//2
            ptr2 = i-i//2
            while ptr1>=0 and ptr2<len(s) and s[ptr1]==s[ptr2]:
                    ptr1 -= 1
                    ptr2 += 1
            if ptr2-ptr1-1>ans:
                ans=ptr2-ptr1-1
                index=[ptr1+1,ptr2]
                
        return s[index[0]:index[1]]