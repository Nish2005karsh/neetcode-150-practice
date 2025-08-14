def singleNumber(nums):
    XOR=0
    for i in nums:
        XOR^=i
    return XOR
nums=[4,1,2,1,2]
print(singleNumber(nums))