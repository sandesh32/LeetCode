from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i in words:
            d[i[0]].append(i)
        ans = 0
        for c in s:
            temp = d[c]
            d[c] = []
            for i in temp:
                if len(i) == 1:
                    ans += 1
                else:
                    d[i[1]].append(i[1:])
        return ans