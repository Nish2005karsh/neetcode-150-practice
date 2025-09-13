# def duplicateNums(nums):
#     nums.sort()
#     for i in range(len(nums)-1):
#         for j in range(1,len(nums)):
#             if  nums[i]==nums[j]:
#                 return True
#     return False



# nums=[1,2,3,1]
# print(duplicateNums(nums))
# via set
def duplicateNums(nums):
    if(len(nums)!=len(set(nums))):
        return True
    return False
    
nums=[1,2,3,1]
print(duplicateNums(nums))
