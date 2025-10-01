class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # your code here
        min_price = float('inf')
        max_profit = 0