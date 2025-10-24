# def missingNumber(nums):
#     n=len(nums)
#     expected_sum=n*(n+1)//2
#     actual_sum=sum(nums)
#     return expected_sum-actual_sum
# nums=[3,0,1]
# print(missingNumber(nums))

# def missingNumber(nums):
#     nums.sort()
#     for idx,val in enumerate(nums):
#         if idx!=val:
#             return val-1
#         if(len(nums)-1==val):
#             return val+1
# nums=[3,0,1]
# print(missingNumber(nums))

# via xor
def missingNumber(nums):
    res=len(nums)
    for i in range(len(nums)):
        res^=i^nums[i]
    return res
nums=[3,0,1]
print(missingNumber(nums))
