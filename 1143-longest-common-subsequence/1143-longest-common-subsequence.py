class Solution(object):
    def recur(self, text1, text2, n, m, dp):
        if n == 0 or m == 0:
            return 0
        
        if dp[n][m] != -1:
            return dp[n][m]

        if text1[n-1] == text2[m-1]:
            dp[n][m] = 1 + self.recur(text1, text2, n-1, m-1, dp)
        else:
            dp[n][m] = max(self.recur(text1, text2, n-1, m, dp),
                           self.recur(text1, text2, n, m-1, dp))
        
        return dp[n][m]
        
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)

        dp = [[-1] * (m+1) for _ in range(n+1)]
        return self.recur(text1, text2, n, m, dp)
