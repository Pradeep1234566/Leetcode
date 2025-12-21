class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zeroes = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append([i,j])
        
        for row, column in zeroes:
            for i in range(n):
                matrix[row][i] = 0
            
            for i in range(m):
                matrix[i][column] = 0
        
        
        
