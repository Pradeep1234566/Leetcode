class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        seen = set()
        rows = len(board)
        columns = len(board[0])

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == '.':
                    continue
                
                number = board[i][j]

                row_key = ('row', i, number)
                column_key = ('column', j, number)

                box_key = ('box', i // 3, j // 3, number)

                if row_key in seen or column_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)
        
        return True
        