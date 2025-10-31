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
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if not nums or len(nums) < 3:
#             return []
#         nums.sort()
#         res = []
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 curr_sum = nums[i] + nums[left] + nums[right]
#                 if curr_sum == 0:
#                     res.append([nums[i], nums[left], nums[right]])
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1

#                     left += 1
#                     right -= 1
#                 elif curr_sum < 0:
#                     left += 1
#                 else:
#                     right -= 1

#         return res
# Bit manipulation
# Single number
# nums=[2,2,1] op->1
# def singleNumber(nums):
#     xor=0
#     for num in nums:
#         xor^=num
#     return xor 
# def singleNumber(nums):
#     seen=set()
#     for num in nums:
#         if num in seen:
#             seen.remove(num)
#         else:
#             seen.add(num)
# Hamming weight
# n = 11 binary->1011 op->3
# def hammingWeight(n):
#     return bin(n).count('1')
# Integer.bitCount() use in java
# Count bits
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# def countBits(n):
#     res = [0] * (n + 1)  [0,0,0,0]
#     for i in range(1, n + 1): i=1,2
#         res[i] = res[i >> 1] + (i & 1) 
#     return res
# def countBits(n):
#     res = []
#     for i in range(n + 1):
#         res.append(bin(i).count('1'))
#     return res
# import java.util.*;
# public class Solution {
#     public int[] countBits(int n) {
#         int[] res = new int[n + 1]; // create an array of size n+1
#         for (int i = 0; i <= n; i++) {
#             res[i] = Integer.bitCount(i); // count number of 1's in binary
#         }
#         return res;
#     }
#     public static void main(String[] args) {
#         Solution sol = new Solution();
#         int n = 5;
#         int[] result = sol.countBits(n);
#         System.out.println(Arrays.toString(result)); // [0, 1, 1, 2, 1, 2]
#     }
# }
# Reverse Bits
# def reverseBits(n):
#     result=0
#     for i in range(32):
#         result<<=1
#         result|=(n&1)
#         n>>=1
#     class Solution {
#     public int reverseBits(int n) {
#         int res=0;
#         for(int i=0;i<32;i++){
#             int lsb=n&1;
#             int rev_lsb=lsb<<(31-i);
#             res=res| rev_lsb;
#             n=n>>1;

#         }
#         return res;
        
#     }
# }
# Missing Number
# def missingNumber(nums):
#     n=len(nums)
#     total=n*(n+1)//2
#     sum_nums=sum(nums)
#     return total-sum_nums
# 2nd method
# def missingNumber(nums):
#     missing = len(nums) n=3
#     for i, num in enumerate(nums): {0:3,1:0,2:1}
#         missing ^= i ^ num  missing=3^0^3=0  misisng=0^1^0=1 missing=1^2^1=2
#     return missing
# Input: nums = [3,0,1]
# Output: 2
# class Solution {
#     public int getSum(int a, int b) {
#         while(b!=0){
#             int carry=a & b;
#             a=a^b;
#             b=carry<<1;

#         }
#         return a;
       
        
#     }
# }
# Greedy algorithm
# from typing import List
# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()
#         s.sort()
#         i = j = 0
#         while i < len(g) and j < len(s):
#             if s[j] >= g[i]: 
#                 i += 1        
#             j += 1           
        
#         return i 
   
# Gas station
# def canCompleteCircuit(gas,cost):
#     if sum(gas)<sum(cost):
#         return -1
#     total=0
#     res=0
#     for i in range(len(gas)):
#         total+=gas[i]-cost[i]
#         if total < 0:
#             total=0
#             res=i+1
#         return res
# graph numericals
# Inorder traversal




   


    

     

   
   



    








