class Solution(object):
    def solve(self, nums, target,dp):
        if target == 0:
            return 1

        if target < 0:
            return 0

        total = 0
        
        if target in dp:
            return dp[target]

        for num in nums:
            if num <= target:
                total += self.solve(nums, target - num, dp)
                
        dp[target] = total
        return total

    def combinationSum4(self, nums, target):
        dp = {}
        return self.solve(nums, target, dp)