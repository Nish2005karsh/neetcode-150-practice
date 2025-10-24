def  longestConsequtive(nums):
    num_set=set(nums)
    longest=0
    for n in num_set:
        if n-1 not in num_set:
            length=0
            while n+length in num_set:
                length+=1
            longest=max(longest,length)
    return longest
nums=[100,4,200,1,3,2]
print(longestConsequtive(nums))

# corresponing java code full code in java 

