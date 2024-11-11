class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 10001
        sell = 0
        profit = 0
        for i in prices:
            if i < buy or i < sell:
                if sell > 0:
                    profit += sell - buy
                buy = i
                sell = 0
            elif i > sell:
                sell = i
        if sell > 0:
            profit += sell - buy
        return profit
