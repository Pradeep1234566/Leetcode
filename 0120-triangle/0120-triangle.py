class Solution:
    def helper(self, triangle, row, ir, ic, dp):
        if ir == row - 1:
            return triangle[ir][ic]

        if (ir, ic) in dp:
            return dp[(ir, ic)]

        down = self.helper(triangle, row, ir + 1, ic, dp)
        diagonal = self.helper(triangle, row, ir + 1, ic + 1, dp)

        dp[(ir, ic)] = triangle[ir][ic] + min(down, diagonal)

        return dp[(ir, ic)]

    def minimumTotal(self, triangle):
        row = len(triangle)
        dp = {}
        return self.helper(triangle, row, 0, 0, dp)