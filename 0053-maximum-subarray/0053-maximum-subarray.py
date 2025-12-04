class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maximum = float('-inf')

        for i in range(len(nums)):
            total += nums[i] 
            if total < 0:
                maximum = max(total, maximum)
                total = 0
            else:
                maximum = max(maximum, total)
        
        return maximum
                