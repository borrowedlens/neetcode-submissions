class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        profit = 0
        while s < len(prices):
            if prices[s] > prices[b]:
                profit = max(profit, prices[s] - prices[b])
            else:
                b = s
            s += 1
        return profit