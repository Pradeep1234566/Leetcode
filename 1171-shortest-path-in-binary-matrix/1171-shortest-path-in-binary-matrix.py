from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        columns = len(grid[0])
        visited = [[0 for _ in range(columns)] for _ in range(rows)]
        visited[0][0] = 1

        queue = deque([(0, 0, 1)])  
        directions = [
            (1, 1), (-1, -1), (0, 1), (0, -1),
            (1, 0), (-1, 0), (-1, 1), (1, -1)
        ]

        while queue:
            r, c, dist = queue.popleft()

            
            if r == rows - 1 and c == columns - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 0 and visited[nr][nc] == 0:
                    queue.append((nr, nc, dist + 1))
                    visited[nr][nc] = 1

        return -1  
