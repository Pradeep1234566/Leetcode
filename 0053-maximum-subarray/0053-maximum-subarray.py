class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        N = len(nums)
        maximum_sum = float('-inf')

        for i in range(N):
            total += nums[i]

            if total < 0:
                maximum_sum = max(maximum_sum, total)
                total = 0
            
            else:
                maximum_sum = max(maximum_sum, total)
        
        return maximum_sum
