# Two sum
# def twoSum(nums,tar):
#     hashmap={}
#     for i in range(len(nums)):
#         if tar-nums[i] in hashmap:
#             return [hashmap[tar-nums[i]],i]
#         hashmap[nums[i]]=i
# Time o buy and sell stock
# prices=[7,1,5,3,6,4]
# def maxProfit(prices):
#     curr_price=prices[0] 
#     max_profit=0
#     for i in range(1,len(prices)):[1,5,3,6,4]
#         if prices[i]<curr_price: 1<7 true 5<1 false
#             curr_price=prices[i]  curr_price=1 
#         else:
#             max_profit=max(max_profit,prices[i]-curr_price) max_profit=max(0,5-1)=4

#     return max_profit
# Done using sliding window 
# Using two pointers
# [7,1,5,3,6,4]
# l=0,r=1 r<length of prices  mzxp=0 prices[right]>prices[left] mean high sell price and low buy prices profit max profit then if prices[right]<prices[left] then l=r and right+=1
# class Solution {
#     public int maxProfit(int[] prices) {
#         int left = 0;  // buy day  
#         int right = 1; // sell day
#         int maxProfit = 0;
#         while (right < prices.length) {
#             if (prices[right] > prices[left]) {     1>7 false
#                 int profit = prices[right] - prices[left];     []
#                 maxProfit = Math.max(maxProfit, profit);
#             } else {
#                 left = right; // move left to a cheaper buying price l=1 r=2
#             }
#             right++;
#         }
#         return maxProfit;
#     }
# }

# Move Zeroes
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# def moveZeroes(nums):
#     left=0
#     for right in range(len(nums)):
#         if nums[right]!=0:
#             nums[left],nums[right]=nums[right],nums[left]
#             left+=1

# Valid paranthesis
# def isValid(s):
#     stack=[]
#     for char in s:
#         if char == '(':
#             stack.append(')')
#         elif char=='{':
#             stack.append('}')
#         elif char== "[":
#             stack.append(']')
#         else:
#             if not stack or stack.pop()!=char:
#                 return False
#     return len(stack)==0
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.minStack or val <= self.minStack[-1]:
#             self.minStack.append(val)

#     def pop(self) -> None:
#         popped_val = self.stack.pop()
#         if popped_val == self.minStack[-1]:
#             self.minStack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.minStack[-1]
# Product of array except self
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# def product(nums):
#    n=len(nums)
#    left=[1]*n
# #    [1,1,1,1]
#    right=[1]*n
#    ans=[1]*n
# #    left loop
#     for i in range(1,n):
#         left[i]=left[i-1]*nums[i-1]
#     # Right loop
#     for i in range(n-2,-1,-1):
#         right[i]=right[i+1]*nums[i+1]
#     for i in range(n):
#         ans[i]=left[i]*right[i]

# def twoSum2(nums,target):
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
# nums=[2,7,11,15]
# target=9
# print(twoSum2(nums,target))
def threeSum(nums):
    if(nums==None or len(nums)<3):
        return []
    

     

   
   



    








