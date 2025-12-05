from collections import deque

class Solution(object):

    def orangesRotting(self, grid):
        Row = len(grid)
        Column = len(grid[0])

        queue = deque()

       
        for i in range(Row):
            for j in range(Column):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))   

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while queue:
            r, c, t = queue.popleft()
            minutes = max(minutes, t)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < Row and 0 <= nc < Column and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, t + 1))

        for row in grid:
            if 1 in row:
                return -1

        return minutes
