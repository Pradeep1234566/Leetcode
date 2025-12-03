class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s[::-1]

        n = len(s)
        m = len(temp)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == temp[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return n - dp[n][m]
        