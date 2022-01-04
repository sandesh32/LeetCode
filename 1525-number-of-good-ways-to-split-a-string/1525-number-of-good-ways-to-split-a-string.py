class Solution:
    def numSplits(self, s: str) -> int:
        answer = 0
        first_to_last = collections.Counter()
        last_to_first = {}
        for i in s:
            if i not in last_to_first:
                last_to_first[i]=1
            else:
                last_to_first[i]+=1
        for c in s:
            first_to_last[c] += 1
            last_to_first[c] -= 1
            if last_to_first[c] == 0:
                del last_to_first[c]
            if len(first_to_last) == len(last_to_first):
                answer += 1
        return answer
