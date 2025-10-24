def add(a,b):
    while b!=0:
        carry=a&b
        a=a^b
        b=carry<<1
    return a
a,b=2,3
print(add(a,b))
# Complexity i
