class Solution(object):
    def helper(self, m, n, dp):
        # If we reach top-left cell → 1 path
        if m == 0 and n == 0:
            return 1
        
        # Out of bounds → no path
        if m < 0 or n < 0:
            return 0
        
        # Already computed
        if (m, n) in dp:
            return dp[(m, n)]
        
        # Move up and left
        top = self.helper(m - 1, n, dp)
        left = self.helper(m, n - 1, dp)
        
        dp[(m, n)] = top + left
        return dp[(m, n)]

    def uniquePaths(self, m, n):
        return self.helper(m - 1, n - 1, {})
