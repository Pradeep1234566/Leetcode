class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        maximum_sum = float('-inf')
        N = len(nums)
        # if N == 1:
        #     return nums[0]

        for i in range(N):
            total += nums[i]
            maximum_sum = max(maximum_sum, total)
            if total < 0:
                total = 0
        
        return maximum_sum
                