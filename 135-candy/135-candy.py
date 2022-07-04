class Solution:
    def candy(self, rat: List[int]) -> int:
        arr = [1 for i in range(len(rat))]
        for i in range(1, len(rat)):
            if rat[i]>rat[i-1]:
                arr[i] = arr[i-1] + 1
        ans = arr[-1]
        for i in range(len(rat)-2,-1,-1):
            if rat[i]>rat[i+1]:
                arr[i] = max(arr[i],arr[i+1] + 1)
            ans += arr[i]
        return ans