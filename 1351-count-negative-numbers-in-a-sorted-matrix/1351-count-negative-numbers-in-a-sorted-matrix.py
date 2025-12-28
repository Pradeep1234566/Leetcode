class Solution(object):
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        i = rows - 1
        j = 0
        count = 0

        while i >= 0 and j < cols:
            if grid[i][j] < 0:
                count += cols - j
                i -= 1
            else:
                j += 1

        return count
