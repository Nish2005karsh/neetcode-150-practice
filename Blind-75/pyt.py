# Blind 75 numericals practice
# 1.Two sum
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for  j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# nums = [2, 7, 11, 15]
# target = 9
# Using two pointer
# def twoSum(nums,target):
#     left=0
#     right=len(nums)-1
#     while left<=right:
#         if nums[left]+nums[right]==target:
#             return [left,right]
#         elif nums[left]+nums[right]<target:
#             left+=1
#         else:
#             right-=1    
# nums = [2, 7, 11, 15] 
    
# 2.Contains duplicatre
def containsDuplicate(nums):
    if len(nums)!=len(set(nums)):
        return True
    return False
# nums = [1,2,3,1]
def containsduplicate(nums):
    nums.sort()
    for i in nums:
        if nums[i]==nums[i+1]:
            return True
    return False
# nums = [1,2,3,1]
# 3.No of 1 bits
def hammingWeight(n):
    return bin(n).count('1')
# 2 nd method
def hammingWeight(n):
    count=0
    k=bin(n)[2:]
    for i in k:
        if i=="1":
            count+=1
    return count
# 4.Missing number
def missingNumber(nums):
    n=len(nums)
    return n*(n+1)//2-sum(nums)

# 5.Valid anagram
def isValidAnagram(s,t):
    return sorted(s)==sorted(t)

#6.Valid palindrome
def isPallindrome(s) :
    i,j=0,len(s)-1
    while i<j:
        while i<j and not s[i].isalnum():
            i+=1
        while i<j and not s[j].isalnum():
            j-=1
        if s[i].lower()!=s[j].lower():
            return False
        i,j=i+1,j-1
    return True



