class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count0 = s.count('0')
        tot = 0
        count1 = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                temp = 2**(len(s)-1-i)
                if tot+temp>k:
                    return count0+count1
                tot+=temp
                count1+=1
        return count0+count1