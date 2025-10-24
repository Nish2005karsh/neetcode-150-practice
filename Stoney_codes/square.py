def squares(nums):
    k=[x*x for x in nums]
    return sorted(k)
nums=[-4,-3,0,3,10]
print(squares(nums))