class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)

        # dp same shape as triangle
        dp = [row[:] for row in triangle]

        # start from second last row
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]
