# Set bits are the bits consisting 1 
def Numberof1Bits(n):
    k=bin(n)
    count=0
    for i in k[2:]:
        if i =="1":
            count+=1
    return count
n=11
print(Numberof1Bits(n))
# Time complexity is O(logn)
# Other methof
def Numberof1Bits(n):
    count=0
    while n:
        n=n&(n-1)
        count+=1
    return count
n=11
print(Numberof1Bits(n))

# O(logn)
# Finding binary without bin
n=11
while n:
    print(n&1,end="")
    n=n>>1

    

