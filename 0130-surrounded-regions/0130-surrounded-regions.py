class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])

        queue = deque()

        for row in range(rows):
            for column in [0, columns-1]:
                if board[row][column] == 'O':
                    queue.append([row,column])
                    board[row][column] = 'T'                
        
        for column in range(columns):
            for row in [0, rows-1]:
                if board[row][column] == 'O':
                    queue.append([row,column])
                    board[row][column] = 'T'
                
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0<=nr<rows and 0<=nc<columns and board[nr][nc] == 'O':
                    queue.append([nr,nc])
                    board[nr][nc] = 'T'
                
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

            
        return board