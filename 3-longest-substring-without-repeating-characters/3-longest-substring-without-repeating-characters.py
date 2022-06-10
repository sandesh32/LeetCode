class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ptr = 0
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                ans = max(ans, i-ptr)
                if d[s[i]]+1>ptr:
                    ptr = d[s[i]]+1
                d[s[i]]=i
        return max(ans,len(s)-ptr)