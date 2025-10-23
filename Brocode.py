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





