class Solution(object):
    def helper(self, obstacleGrid, r, c, dp):
        
        if r < 0 or c < 0:
            return 0
        
       
        if obstacleGrid[r][c] == 1:
            return 0
        
       
        if r == 0 and c == 0:
            return 1
        
        
        if dp[r][c] != -1:
            return dp[r][c]        
        
        top = self.helper(obstacleGrid, r - 1, c, dp)
        left = self.helper(obstacleGrid, r, c - 1, dp)
        
        dp[r][c] = top + left
        return dp[r][c]

    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        dp = [[-1]*(columns) for _ in range(rows)]

        return self.helper(obstacleGrid, rows - 1, columns - 1, dp)
