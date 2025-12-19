class Solution(object):
    def maxProfit(self, nums):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProf = 0
        minimum_price = float('inf')
        N = len(nums)


        for i in range(N):
            minimum_price = min(minimum_price, nums[i])
            maxProf = max(maxProf, nums[i] - minimum_price)
        
        return maxProf