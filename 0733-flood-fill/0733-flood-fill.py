from collections import deque

class Solution(object):
    def dfs(self, image, sr, sc, color, rows, columns, old_color):

        if sr < 0 or sc <0 or sr>=rows or sc>=columns:
            return 
        
        if image[sr][sc] != old_color:
            return 
    
        image[sr][sc] = color
        
        self.dfs(image, sr+1, sc, color, rows, columns, old_color)
        self.dfs(image, sr-1, sc, color, rows, columns, old_color)
        self.dfs(image, sr, sc+1, color, rows, columns, old_color)
        self.dfs(image, sr, sc-1, color, rows, columns, old_color)

    
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]

        if old_color == color:
            return image
        
        rows = len(image)
        columns = len(image[0])

        self.dfs(image, sr, sc, color, rows, columns, old_color)

        return image