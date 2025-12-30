class Solution(object):
    def is_safe(self, row, column, diag1, diag2, COLUMN):
        if column not in COLUMN and (row + column) not in diag1 and (row - column) not in diag2:
            return True
        return False

    def solve(self, n, row, diag1, diag2, COLUMN):
        if row == n:
            return 1   # one valid arrangement found

        count = 0

        for col in range(n):   # FIX 1
            if self.is_safe(row, col, diag1, diag2, COLUMN):
                COLUMN.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                count += self.solve(n, row + 1, diag1, diag2, COLUMN)

                COLUMN.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        return count

    def totalNQueens(self, n):
        COLUMN = set()
        diag1 = set()
        diag2 = set()

        return self.solve(n, 0, diag1, diag2, COLUMN)
