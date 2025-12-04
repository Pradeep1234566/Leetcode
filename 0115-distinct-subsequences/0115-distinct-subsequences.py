class Solution(object):
    def helper(self, s, t, n, m, dp):
        if m == 0:
            return 1
        if n == 0:
            return 0
        
        if dp[n][m] != -1:
            return dp[n][m]
        
        if s[n-1] == t[m-1]:
            include = self.helper(s,t,n-1,m-1,dp)
            exclude = self.helper(s,t,n-1,m,dp)
            dp[n][m] = include + exclude
        
        else:
            dp[n][m] = self.helper(s,t,n-1,m,dp)
        
        return dp[n][m]

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)

        dp = [[-1]*(m+1) for _ in range(n+1)]

        return self.helper(s,t,n,m,dp)