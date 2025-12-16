class Solution(object):
    def helper(self, row, column, grid, dp):
        if row < 1 or column < 1:
            return float('inf')
        
        if row == 1 and column == 1:
            return grid[row-1][column-1]
        

        if dp[row][column] != -1:
            return dp[row][column]

        up_way = grid[row-1][column-1] + self.helper(row-1, column, grid, dp)

        left_way = grid[row-1][column-1] + self.helper(row, column-1, grid, dp)

        dp[row][column] = min(up_way, left_way)

        return dp[row][column]

        


        
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
      
        dp = [[-1]*(columns+1) for _ in range(rows+1)]
        return self.helper(rows, columns, grid, dp)

        