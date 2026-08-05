class Solution(object):
    def helper(self, index, nums, n, dp):
        if index == n - 1:
            return nums[index]
        
        if index >= n:
            return 0
        
        if index in dp:
            return dp[index]

        pick = nums[index] + self.helper(index+2, nums, n, dp)

        not_pick = self.helper(index+1, nums, n, dp)

        dp[index] = max(pick, not_pick)

        return dp[index]
        
    def rob(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        return self.helper(0, nums, len(nums), dp)
