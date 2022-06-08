class Solution(object):
    def setZeroes(self, matrix):
        is_col = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if j==0:
                        is_col=True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                    
                    
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        if matrix[0][0]==0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        
        if is_col:
            for r in range(len(matrix)):
                matrix[r][0]=0
