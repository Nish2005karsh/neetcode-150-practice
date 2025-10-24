# Contains all stoney codes lesson
# Day1:
# 1.Duplicate values in array
def containsDuplicate(nums):
    return len(nums)!=len(set(nums))
# 2.Missing number
def missingNumber(nums):
    n=len(nums)
    return n*(n+1)//2-sum(nums)
# 2 nd methof
def missingNumber(nums):
    return list(set(range(len(nums)+1))-set(nums))
# 3.

