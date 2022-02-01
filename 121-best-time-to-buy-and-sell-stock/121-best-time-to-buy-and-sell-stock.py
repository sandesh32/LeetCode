class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index=len(prices)-1
        profit=0
        for i in range(len(prices)-2,-1,-1):
            if prices[index]-prices[i]>=profit:
                profit=prices[index]-prices[i]
            else:
                if prices[i]>prices[index]:
                    index=i
        return profit