class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, lowestday = prices[0], 0
        highest, highestday = prices[0], 0
        # if the lowest price came before the highest
        # we buy

        max = 0
        for i in range(len(prices)-1):
            for n in range(i+1,len(prices)):
                if (prices[i] < prices[n]) and (prices[n]-prices[i] > max):
                    max = prices[n]-prices[i]

        return max

