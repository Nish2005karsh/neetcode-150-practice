# Amazon sde sheet by ridhi  dutta
# 1.Third maximum number
# def thirdMax(nums):
#     set_nums=sorted(nums)
#     if len(set_nums)<3:
#         return set_nums[-1]
#     return set_nums[-3]
# nums=[3,2,1]
# print(thirdMax(nums))
# 2.Product of array except self
# def productExceptSelf(nums):
#     n=len(nums)
#     left=[1]*n
#     right=[1]*n
#     ans=[1]*n
#     # For left part
#     for i in range(1,n):
#         left[i]=left[i-1]*nums[i-1]
#     for i in range(n-2,-1,-1):
#         right[i]=right[i+1]*nums[i+1]
#     for i in range(n):
#         ans[i]=left[i]*right[i]
#     return ans
# 3.Two sum 2
# using two pointers
# def twoSum(nums,target):
#     nums.sort()
#     left=0
#     right=len(nums)-1
#     while left<right:
#         curr_sum=nums[left]+nums[right]
#         if curr_sum==target:
#             return [left+1,right+1]
#         elif curr_sum>target:
#             right-=1
#         else:
#             left+=1
# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap={}
    #     for  i in range(len(nums)):
    #         if(target-nums[i] in hashmap):
    #             return [hashmap[target-nums[i]],i]
    #         hashmap[nums[i]]=i
    #     return []
    
# Trapping rain water
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l_wall=0
#         r_wall=0
#         n=len(height)
#         max_left=[0]*n
#         max_right=[0]*n
#         for i in range(n):
#             j=-i-1
#             max_left[i]=l_wall
#             max_right[j]=r_wall
#             l_wall=max(l_wall,height[i])
#             r_wall=max(r_wall,height[j])
#         summ=0
#         for i in range(n):
#             pot=min(max_left[i],max_right[i])
#             summ+=max(0,pot-height[i])
#         return summ
# Missing Number
# def missingNumber(nums):
#     n=len(nums)
#     total_sum=n*(n+1)//2
#     curr_sum=sum(nums)
#     return total_sum-curr_sum
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         missing=len(nums)
#         for i,num in enumerate(nums):
#             missing ^= i ^ num
#         return missing