class Solution(object):
    def helper(self, row, column, index, ROW, COLUMN, word, board):
        if index == len(word):
            return True
        
        if row < 0 or row >= ROW or column < 0 or column >= COLUMN or board[row][column] != word[index]:
            return False

        temp = board[row][column]
        board[row][column] = '#'  # mark as visited

        found = (self.helper(row+1, column, index+1, ROW, COLUMN, word, board) or
                 self.helper(row-1, column, index+1, ROW, COLUMN, word, board) or
                 self.helper(row, column+1, index+1, ROW, COLUMN, word, board) or
                 self.helper(row, column-1, index+1, ROW, COLUMN, word, board))

        board[row][column] = temp  # backtrack
        return found

    def exist(self, board, word):
        ROW = len(board)
        COLUMN = len(board[0])

        for i in range(ROW):
            for j in range(COLUMN):
                if self.helper(i, j, 0, ROW, COLUMN, word, board):
                    return True

        return False
