def maxProfit(prices):
    l,r=0,1
    maxP=0
    while r!=len(prices):
        if prices[l]<prices[r]:
            # 7<1 condition false
            # 1<5 condition tru
            prof=prices[r]-prices[l]
            maxP=max(maxP,prof)
        else:
            l=r
        r+=1
    return maxP
prices=[7,1,5,3,6,4]
print(maxProfit(prices))