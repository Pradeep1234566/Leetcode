class Solution(object):
    def maxMatrixSum(self, matrix):
        count = 0
        min_abs = float('inf')
        total = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    count += 1
                min_abs = min(min_abs, abs(val))

        if count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
