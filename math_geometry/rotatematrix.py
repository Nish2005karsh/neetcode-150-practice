# using 4 way exchange
def rotateimage(matrix):
    n = len(matrix)
    for i in range((n+1)//2):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
    return matrix

# Time complexity is O(n^2)
# Space complexity is O(1)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotateimage(matrix))

# Second method
def rotateimage(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
    return matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotateimage(matrix))