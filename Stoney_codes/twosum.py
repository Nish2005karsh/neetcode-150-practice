# def twoSum(nums,tar):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==tar:
#                 return [i,j]
#             else:
#                 return []
# nums=[2,7,11,15]
# tar=9
# print(twoSum(nums,tar))

# Second method 
# Using hashmap
# def twoSum(nums):
#     hash_map={}
#     for  idx,val in enumerate(nums):
#         diff=tar-val
#         if diff in hash_map:
#             return [hash_map[diff],idx]
#         hash_map[val]=idx  
# nums=[1,2,3,4]
# tar=9
# print(twoSum(nums,tar))

# Using 2 pointer technique
def twoSum(nums,tar):
    nums.sort()
    i,j=0,len(nums)-1
    while(i<j):
        sum1=nums[i]+nums[j]
        if(sum1==tar):
            return [i,j]
        elif(sum1>tar):
            j-=1
        else:
            i+=1
    return False
nums=[2,11,7,15]
tar=9
print(twoSum(nums,tar))