def setMatrixZero(matrix):
    first_row_has_zero=False
    first_column_has_zero=False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==0):
                if(i==0):
                    first_row_has_zero=True
                if(j==0):
                    first_column_has_zero=True
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if(matrix[i][0]==0 or matrix[0][j]==0):
                matrix[i][j]=0
    if(first_row_has_zero):
        for j in range(len(matrix[0])):
            matrix[0][j]=0
    if(first_column_has_zero):
        for i in range(len(matrix)):
            matrix[i][0]=0
    return matrix
matrix=[[1,1,1],[1,0,1],[1,1,1]]
print(setMatrixZero(matrix))
# Time complexity is O(n^2)
# Space complexity is O(1)


