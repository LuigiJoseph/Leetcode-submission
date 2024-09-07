class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        #2 pointer approach l,r
        #if r value is bigger than l, move to next indices

        l , r = 0, 1 #left = buy, right = sell
        maxProfit = 0


        while r < len(prices):
            #is it profitable?
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            #not profitable
            else:
                l = r
            r += 1
        return maxProfit
                
  