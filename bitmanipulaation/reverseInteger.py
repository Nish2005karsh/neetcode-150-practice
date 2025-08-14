def reverseInteger(num):
    rev=0
    while(num!=0):
        digit=num%10
        if(rev<-2147483648 or rev>2147483647):
            return 0
        rev=rev*10+digit
        num=num//10
    return rev
num=3210
print(reverseInteger(num))