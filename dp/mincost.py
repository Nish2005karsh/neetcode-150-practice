def minCostClimbingStairs(cost):
    n=len(cost)
    dp=[0]*(n+1)
    dp[0]=dp[1]=0
    # Because we can start from step 1 or step 2 and they are free
    for i in range(2,n+1):
        dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[n]
cost=[10,15,20]
print(minCostClimbingStairs(cost))
