class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        
        dp = [[0] * n for _ in range(n)]

        # base case: first row
        for col in range(n):
            dp[0][col] = matrix[0][col]

        # fill dp table row by row
        for row in range(1, n):
            for col in range(n):
                best = dp[row - 1][col]
                if col > 0:
                    best = min(best, dp[row - 1][col - 1])
                if col < n - 1:
                    best = min(best, dp[row - 1][col + 1])
                
                dp[row][col] = matrix[row][col] + best

        return min(dp[n - 1])
