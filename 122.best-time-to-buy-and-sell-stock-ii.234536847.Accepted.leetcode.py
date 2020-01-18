class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        i = 0
        valley = peak = prices[0]
        maxProfit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit

    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit
