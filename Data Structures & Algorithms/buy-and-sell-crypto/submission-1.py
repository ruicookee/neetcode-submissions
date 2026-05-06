class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        maxprofit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                if (prices[sell]-prices[buy] > maxprofit):
                    maxprofit = prices[sell]-prices[buy]
            else:
                buy = sell
            sell += 1
        return maxprofit
                


