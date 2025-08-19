def findMin(arr):
    lo, hi = 0, len(arr) - 1 
    while lo < hi:
        if arr[lo] < arr[hi]:
            return arr[lo]
        mid = (lo + hi) // 2
        if arr[mid] > arr[hi]:
            # Minimum must be in the right half
            lo = mid + 1
        else:
            hi = mid

    return arr[lo]
arr=[3,4,5,1,2]
print(findMin(arr))