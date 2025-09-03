def maxProfit(prices):
    curr_price=prices[0]
    max_profit=0
    for i in range(1,len(prices)):
        if(prices[i]<curr_price):
            # ex->2<7
            curr_price=prices[i]
        else:
            #2>1
            curr_profit=prices[i]-curr_price
            max_profit=max(max_profit,curr_profit)
    return max_profit

prices=[7,1,5,3,6,4]
print(maxProfit(prices))
# Two pointer
def maxProfit(prices):
        # Using the approach of two pointers
        l,r=0,1#Left=>Buy and Right=>sell
        maxProfit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                #Buy low and sell hight=Profit
                profit=prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            r+=1
        return maxProfit


prices=[7,1,5,3,6,4]
print(maxProfit(prices))         