class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        n = len(nums)
        difference = 0

        for i in range(n):
            if i == 0:
                buying = nums[i]
            
            else:
                difference = nums[i] - buying
                maxProfit = max(maxProfit, difference)
                
                buying = min(buying, nums[i])
        
        return maxProfit

            

        