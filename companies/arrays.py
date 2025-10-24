# This consists of the array questions frequently being asked  in interviews
#1. Missing number from 1 to 5
# def missingNums(nums):
#     n=len(nums)+1
#     org_sum=n*(n+1)//2
#     curr_sum=sum(nums)
#     return org_sum-curr_sum
# nums=[1,2,3,5]
# print(missingNums(nums))
#2.Multiple missing values
# def missingNums(nums):
#     n = len(nums) + 2  
#     full_set = set(range(1, n + 1))
#     nums_set = set(nums)
#     return list(full_set - nums_set)

# nums = [1, 2, 4, 6]
# print(missingNums(nums))  
#3 Find all pair of integers whose sum is equal to given number
# def twoSum(nums,tar):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==tar:
#                 print(i,j)
# nums = [2, 7, 11, 15]
# tar=9
# twoSum(nums,tar)
# using hashmap
# def twoSum(nums,tar):
#     hashmap={}
#     for i in range(len(nums)):
#         hashmap[nums[i]]=i
#         if tar-nums[i] in hashmap:
#             print(hashmap[tar-nums[i]],i)
# nums = [2, 7, 11, 15]
# tar=9
# twoSum(nums,tar)
# 4 .Merge sorted array
# def mergeArrays(arr1,arr2):
#     n=len(arr1)
#     m=len(arr2)
#     temp=[0]*(m+n)
#     for i in range(n):
#         temp[i]=arr1[i]
#     for j in range(m):
#         temp[n+j]=arr2[j]
#     temp.sort()
#     # Redistribute them
#     for  i in range(n):
#         arr1[i]=temp[i]
#     for j in range(m):
#         arr2[j]=temp[n+j]
#     print(arr1)
#     print(arr2)
# arr1 = [1, 3, 4, 5]
# arr2 = [2, 4, 6, 8]
# mergeArrays(arr1,arr2) 

# 2nd method
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         for i in range(n):
#             nums1[m+i]=nums2[i]
#         nums1.sort()

#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
# arr1 = [1, 3, 4, 5]
def thirdMaximum(nums):
    set_nums=sorted(set(nums))
    if len(set_nums)<3:
        return set_nums[-1]
    else:
        return set_nums[-3]
# Leetcode program
from collections import Counter, defaultdict

class Solution:
    def majorityGroup(self, s: str) -> str:
        freq = Counter(s)
        
        groups = defaultdict(list)
        for ch, f in freq.items():
            groups[f].append(ch)
        
        # Find majority group
        best_k, best_group = -1, []
        for k, chars in groups.items():
            if len(chars) > len(best_group) or (len(chars) == len(best_group) and k > best_k):
                best_k, best_group = k, chars
        
        return "".join(best_group)





