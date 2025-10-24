def spiralOrder(matrix):
    # matrix[0] means first row
    ret=[]
    while matrix:
        ret+=matrix.pop(0)
        # [1,2,3]
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix:
            ret+=matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    return ret
    # return ret[::-1]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
    
    

     