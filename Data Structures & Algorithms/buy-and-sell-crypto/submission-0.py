class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0

        for curr_price in prices:
            if curr_price < buy_price:
                buy_price = curr_price
            else:
                max_profit = max(max_profit, curr_price - buy_price)
            
        return max_profit
