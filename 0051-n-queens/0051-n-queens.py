class Solution(object):
    def create_board(self, positions, n):
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(".")
            board.append(row)
        for row, col in positions:
            board[row][col] = "Q"
        result = []
        for row in board:
            row_string = ""
            for cell in row:
                row_string += cell
            result.append(row_string)
        return result
    
    def is_safe(self, row, column, COLUMN, Diag1, Diag2):
        return column not in COLUMN and (row-column) not in Diag1 and (row+column) not in Diag2
    
    def solve(self, n, row, COLUMN, Diag1, Diag2, positions, result):
        if row == n:
            result.append(self.create_board(positions, n))
            return
        
        for column in range(n):
            if self.is_safe(row, column, COLUMN, Diag1, Diag2):
                COLUMN.add(column)
                Diag1.add(row-column)
                Diag2.add(row+column)
                positions.append((row, column))
                # Recursive call to place queen in the next row
                self.solve(n, row + 1, COLUMN, Diag1, Diag2, positions, result)
                # Backtrack: remove queen and unmark positions
                COLUMN.remove(column)
                Diag1.remove(row-column)
                Diag2.remove(row+column)
                positions.pop()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        COLUMN = set()
        Diag1 = set()
        Diag2 = set()
        result = []
        self.solve(n, 0, COLUMN, Diag1, Diag2, [], result)
        return result