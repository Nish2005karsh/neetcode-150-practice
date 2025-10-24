def longestconsecutive(nums):
    
    numsSet=set(nums)
    longest=0
    for n in nums:
        if(n-1 not in numsSet):
            length=0
            while n+length in numsSet:
                length+=1
            longest=max(longest,length)
    return longest
nums=[100,4,200,1,3,2]
print(longestconsecutive(nums))