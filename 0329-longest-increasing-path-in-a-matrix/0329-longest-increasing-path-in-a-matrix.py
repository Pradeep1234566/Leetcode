class Solution(object):

    def helper(self, r, c, rows, columns, matrix, dp):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        best = 1 

        if (r,c) in dp:
            return dp[(r,c)]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0<=nr<rows and 0<=nc<columns and matrix[nr][nc] >  matrix[r][c]:
                total = 1 + self.helper(nr, nc, rows, columns, matrix, dp)
                dp[(r,c)] = max(total, best)
                best = dp[(r,c)]

        return best

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        answer = 0
        rows = len(matrix)
        columns = len(matrix[0])
        dp = {}

        for i in range(rows):
            for j in range(columns):
                answer = max(answer, self.helper(i, j, rows, columns, matrix, dp))

        return answer
        
        