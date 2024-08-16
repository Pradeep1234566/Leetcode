class Solution(object):
    def maxProfit(self, prices):
        k = min(prices)
        index = prices.index(k)  
        if index == len(prices) - 1:
            return 0
        else:
            max = 0 
            for i in range(index, len(prices)):
                if prices[i] > max:
                    max = prices[i]
        return max - k 


    
        