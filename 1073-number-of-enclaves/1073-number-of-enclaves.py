from collections import deque

class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()

        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in [0, columns-1]:
                if grid[row][column] == 1:
                    queue.append((row,column))
                    grid[row][column] = -1
        
        for column in range(columns):
            for row in [0,rows-1]:
                if grid[row][column] == 1:
                    queue.append((row, column))
                    grid[row][column] = -1
                
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<rows and 0<=nc<columns and grid[nr][nc] == 1:
                    grid[nr][nc] = -1
                    queue.append((nr,nc))
            
        count = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    count += 1
        
        return count
