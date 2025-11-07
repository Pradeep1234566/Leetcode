from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows = len(board)
        columns = len(board[0])

        queue = deque()

        # enqueue LEFT/RIGHT borders, use 'O' not '0' and mark as 'T' immediately
        for row in range(rows):
            for column in [0, columns-1]:
                if board[row][column] == 'O':
                    queue.append((row, column))
                    board[row][column] = 'T'   # mark visited/safe
        
        # enqueue TOP/BOTTOM borders, same fix + mark
        for column in range(columns):
            for row in [0, rows-1]:
                if board[row][column] == 'O':
                    queue.append((row, column))
                    board[row][column] = 'T'   # mark visited/safe
                
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        # BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'      
                    queue.append((nr, nc))
       
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        
        return board
