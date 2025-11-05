from collections import deque

class Solution(object):

    def dfs(self, image, queue, r, c, Rows, Columns, old_color, new_color):
        image[r][c] = new_color
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < Rows) and (0 <= nc < Columns) and image[nr][nc] == old_color:
                    image[nr][nc] = new_color
                    queue.append((nr, nc))
            

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        from collections import deque
        old_color = image[sr][sc]
        if old_color == color:  
            return image

        queue = deque([(sr, sc)])
        row = len(image)
        column = len(image[0])
        image[sr][sc] = color

        self.dfs(image, queue, sr, sc, row, column, old_color, color)

        return image
