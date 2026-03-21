class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi = 0
        difference = 0
        n = len(nums)

        for i in range(n):
            if i == 0:
                buying = nums[i]
            
            else:
                difference = nums[i] - buying
                maxi = max(maxi, difference)
                buying = min(buying, nums[i])
        
        return maxi
