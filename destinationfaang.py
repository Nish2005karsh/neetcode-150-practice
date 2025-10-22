# Destination faang
# 1.Two sum
# def twosum(nums,tar):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==tar:
#                 return [i,j]
# nums=[2,7,11,15]
# tar=9
# print(twosum(nums,tar))
# using hashset
# def twoSum(nums,tar):
#     hashmap={}
#     for i in range(len(nums)):
#         if tar-nums[i] in hashmap:
#             return [hashmap[tar-nums[i]],i]
#         hashmap[nums[i]]=i
# nums=[2,7,11,15]
# tar=9
# print(twoSum(nums,tar)):
# def containsduplicate(nums):
#     numset=()
#     for num in nums:
#         if nums in numset:
#             return True
#         numset.add(num)
#     return False
# Longest sequence
# def longestconsecutivesequence(nums):
#     if len(nums) ==0:
#         return 0
#     numset=set(nums)
#     longestsub=1
#     for num in numset:
#         if num-1 in numset:
#             continue
#         else:
#             currentnum=num
#             currentsub=1
#             while num+1 in numset:
#                 currentnum+=1
#                 currentsub+=1
#         longestsub=max(longestsub,currentsub)
#     return longestsub
# nums=[100,4,200,1,3,2]
# print(longestconsecutivesequence(nums))
