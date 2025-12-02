class Solution(object):
    def recur(self, nums, n, k, dp):
        # Corrected base cases
        if n == 0:
            if k == 0 and nums[0] == 0:
                return 2   # +0 or -0
            if k == 0 or nums[0] == k:
                return 1
            return 0
        
        if dp[n][k] != -1:
            return dp[n][k]
        
        if nums[n] <= k:
            include = self.recur(nums, n-1, k-nums[n], dp)
            exclude = self.recur(nums, n-1, k, dp)
            dp[n][k] = include + exclude
        else:
            dp[n][k] = self.recur(nums, n-1, k, dp)
        
        return dp[n][k]

    def findTargetSumWays(self, nums, target):
        total = sum(nums)

        if abs(target) > total:
            return 0

        k = total + target

        if k % 2 != 0:
            return 0

        k //= 2
        n = len(nums)

        dp = [[-1] * (k+1) for _ in range(n)]
        return self.recur(nums, n-1, k, dp)
