class Solution(object):
    def helper(self, nums, target, n, dp):
        if target == 0:
            return True

        if n == 0:
            return False
        
        if dp[n][target] != -1:
            return dp[n][target]
        
        if target >= nums[n-1]:
            dp[n][target] = (self.helper(nums, target-nums[n-1], n-1, dp)or self.helper(nums, target, n-1, dp))
        else:

            dp[n][target] = self.helper(nums, target, n-1, dp)

        return dp[n][target]

    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        

        dp = [[-1] * (target+1) for _ in range(n+1)]

        return self.helper(nums, target, n, dp)
