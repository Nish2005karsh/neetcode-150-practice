def set_bits(n):
    count=0
    while n:
        count+=n&1
        n>>=1
    return count
def count_set_bits(n):
    res=0
    for i in range(1,n+1):
        res+=set_bits(i)
    return res
n=6
print(count_set_bits(n))
# output is 9
# complexit is O(nlogn)