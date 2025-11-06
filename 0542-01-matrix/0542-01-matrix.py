from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        columns = len(mat[0])
        queue = deque()

        distance = [[-1 for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append([i, j]) # This is done so that our BFS begins from index that rea pointing to 0 to get the minimum distance

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            R, C = queue.popleft()
            for dr, dc in directions:
                NR = R + dr
                NC = C + dc
                if 0<=NR<rows and 0<=NC<columns and distance[NR][NC] == -1:
                    distance[NR][NC] = distance[R][C] + 1
                    queue.append([NR, NC])
        
        return distance

                    
