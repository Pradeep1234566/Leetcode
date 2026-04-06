class Solution(object):

        def helper(self, n, dp):
            if n < 0:
                return 0

            if n == 0:
                return 1
            
            if dp[n] != -1:
                return dp[n]

            
            one_step = self.helper(n-1, dp)
            two_step = self.helper(n-2, dp)

            dp[n] = one_step + two_step

            return dp[n]
        
        def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            dp = [-1] * (n+1)
            return self.helper(n, dp)
