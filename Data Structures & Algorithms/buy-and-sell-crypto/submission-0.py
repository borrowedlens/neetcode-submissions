class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            curr_profit = 0
            for j in range(i+1, len(prices)):
                curr_profit = max(curr_profit, prices[j] - prices[i])
            profit = max(profit, curr_profit)
        return profit