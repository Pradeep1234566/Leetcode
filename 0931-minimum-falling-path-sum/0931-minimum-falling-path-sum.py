class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        prev = matrix[0][:]

        for r in range(1, n):
            curr = [float('inf')] * n
            for c in range(n):
                for dc in (-1, 0, 1):
                    pc = c + dc
                    if 0 <= pc < n:
                        curr[c] = min(curr[c], prev[pc] + matrix[r][c])
            prev = curr

        return min(prev)
