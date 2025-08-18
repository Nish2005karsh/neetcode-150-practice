# Brute force
def matrixSearch(matrix,target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==target:
                return True
    return False
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(matrixSearch(matrix,target))

# using binary search 
def matrixSearch(matrix,target):
    if(not matrix):
        return False
    rows,cols=len(matrix),len(matrix[0])
    left,right=0,rows*cols-1
    while left<=right:
        mid=left+(right-left)//2
        midValue=matrix[mid//cols][mid%cols]
        if(midValue==target):
            return True
        elif(midValue<target):
            left=mid+1
        else:
            right=mid-1
    return False
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(matrixSearch(matrix,target))  