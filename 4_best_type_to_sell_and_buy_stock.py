import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        lowest_price = sys.maxsize
        max_profit = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            else:
                profit = price - lowest_price
                max_profit = max(profit, max_profit)

        return max_profit