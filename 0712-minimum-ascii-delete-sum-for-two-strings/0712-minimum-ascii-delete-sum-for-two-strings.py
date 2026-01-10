class Solution(object):
    def helper(self, n, m, s1, s2, dp):
        if n == 0:
            return sum(ord(c) for c in s2[:m])
        
        if m == 0:
            return sum(ord(c) for c in s1[:n])
        
        if dp[n][m] != -1:
            return dp[n][m]
        
        if s1[n-1] == s2[m-1]:
            dp[n][m] = self.helper(n-1, m-1, s1, s2, dp)
        
        else:
            dp[n][m] = min(
                ord(s1[n-1]) + self.helper(n-1, m, s1, s2, dp),
                ord(s2[m-1]) + self.helper(n, m-1, s1, s2, dp)
            )
        
        return dp[n][m]

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n = len(s1)
        m = len(s2)

        dp = [[-1]*(m+1) for _ in range(n+1)]
        return self.helper(n, m, s1, s2, dp)

