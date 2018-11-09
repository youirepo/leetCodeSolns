class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        purchased = False
        buyingPrice, profit = 0, 0
        for i in range(len(prices)-1):
            if ((prices[i] < prices[i+1]) and (purchased != True)):
                # Purchase share
                # Hold until the next stock price is less than current price (prices[i])
                buyingPrice = prices[i]
                purchased = True
            elif ((prices[i] >= prices[i+1]) and (purchased == True)):
                # Time to sell, sell at current price
                profit += (prices[i] - buyingPrice)
                purchased = False
        
        if purchased:
            # Have exhausted the list, sell the last stock price
            profit += (prices[len(prices)-1] - buyingPrice)
            purchased = False
            
        return profit
