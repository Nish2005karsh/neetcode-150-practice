def reverseBits(n):
    res=0
    for i in range(32):
        lsb=n&1
        rev_lsb=lsb<<(31-i)
        res=res| rev_lsb
        n=n>>1
    return res
n=43261596
print(reverseBits(n))
