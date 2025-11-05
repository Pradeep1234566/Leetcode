from collections import deque
class Solution(object):
    def bfs(self, queue, visited, row, column, rows, columns, grid):
        visited[row][column] = 1
        queue.append((row, column))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0<=nr<rows) and (0<=nc<columns) and (visited[nr][nc] !=1) and grid[nr][nc] == '1':
                    self.bfs(queue, visited, nr, nc, rows, columns, grid)
        

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        visited = [[0] * columns for _ in range(rows)]
        count = 0
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1' and visited[i][j] != 1:
                    queue = deque()
                    self.bfs(queue, visited, i, j, rows, columns, grid)
                    count += 1
                
        
        return count