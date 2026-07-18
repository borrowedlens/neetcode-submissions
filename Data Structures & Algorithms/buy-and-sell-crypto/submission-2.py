class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bP = prices[0]
        maxP = 0
        for i in range(1, len(prices)):
            if prices[i] < bP:
                bP = prices[i]
            else:
                maxP = max(maxP, prices[i] - bP)
        return maxP