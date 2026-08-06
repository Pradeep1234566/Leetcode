class Solution(object):
    def helper(self, index, nums, n, dp):
        if index == n-1:
            return nums[index]
        
        if index >= n:
            return 0

        if index in dp:
            return dp[index]
        
        include = nums[index] + self.helper(index+2, nums, n, dp)
        exclude = self.helper(index+1, nums, n, dp)

        dp[index] = max(include, exclude)

        return dp[index]

    def rob(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index = 0
        dp1 = {}
        dp2 = {}

        if n == 1:
            return nums[0]
        return max(self.helper(index, nums[1:], n-1, dp1), self.helper(index, nums[:-1], n-1, dp2))    
    