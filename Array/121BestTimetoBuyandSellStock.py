// the version to understand easily
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        minprice = float('inf')
        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            profit = prices[i] - minprice
            maxprofit = max(profit, maxprofit)
        return maxprofit



//the version of 根据相邻两个数据的差价
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        curprofit = 0
        for i in range(1, len(prices)):
            if(curprofit < 0):
                curprofit = prices[i] - prices[i-1]
            else:
                curprofit += prices[i] - prices[i-1]
            
            maxprofit = max(maxprofit, curprofit)
        return maxprofit
