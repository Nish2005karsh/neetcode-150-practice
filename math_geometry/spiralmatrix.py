def spiralMatrix(matrix):
    rowbegin = 0
    rowend = len(matrix) - 1
    colbegin = 0
    colend = len(matrix[0]) - 1

    res = []
    while rowbegin <= rowend and colbegin <= colend:
        # Traverse Right
        for i in range(colbegin, colend+1):
            res.append(matrix[rowbegin][i])
        rowbegin += 1

        # Traverse Down
        for i in range(rowbegin, rowend+1):
            res.append(matrix[i][colend])
        colend -= 1

        # Traverse Left (check rowbegin <= rowend)
        if rowbegin <= rowend:
            for i in range(colend, colbegin-1, -1):
                res.append(matrix[rowend][i])
            rowend -= 1

        # Traverse Up (check colbegin <= colend)
        if colbegin <= colend:
            for i in range(rowend, rowbegin-1, -1):
                res.append(matrix[i][colbegin])
            colbegin += 1

    return res
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralMatrix(
matrix
))
# Time complexity is O(n^2)
# Space complexity is O(1)


    