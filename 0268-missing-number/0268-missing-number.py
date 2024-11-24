class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        
        real_sum = N * (N+1) // 2
        
        actual_sum = sum(nums)
        
        return real_sum - actual_sum
        