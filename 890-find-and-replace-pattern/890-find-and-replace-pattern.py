class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for w in words:
            d1 = {}
            d2 = {}
            check = True
            for i in range(len(w)):
                if w[i] not in d1:
                    d1[w[i]] = pattern[i]
                elif d1[w[i]] != pattern[i]:
                    check = False
                    break
                if pattern[i] not in d2:
                    d2[pattern[i]] = w[i]
                elif d2[pattern[i]] != w[i]:
                    check = False
                    break
            if check:
                ans.append(w)
        return ans
            
            