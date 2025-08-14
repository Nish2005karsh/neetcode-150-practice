def foundMissingNumber(nums):
    xor_all=0
    xor_nums=0
    for i  in range(0,len(nums)+1):
        xor_all=xor_all^i
    for i in nums:
        xor_nums=xor_nums^i
    return xor_all ^ xor_nums
nums=[3,0,1]
print(foundMissingNumber(nums))
# complexity is O(n)

# Second method
def foundMissingNumber(nums):
    n=len(nums)

    tot_sum=(n*(n+1))//2
    curr_sum=sum(nums)
    return tot_sum-curr_sum
nums=[3,0,1]
print(foundMissingNumber(nums))
# complexity is O(n)
# Third method
def foundMissingNumber(nums):
    res=len(nums)
    for i in range(len(nums)):
        res+=(i-nums[i])
    return res
nums=[3,0,1]
print(foundMissingNumber(nums))