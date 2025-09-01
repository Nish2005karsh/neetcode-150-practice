# House robber 2
def robCircular(nums):
    if len(nums)<2:
        return nums[0]
    # Create two arrays to handle the 2 cases
    # Case 1: Rob the first house and not the last house
    # Case 2: Not rob the first house and rob the last house
    def robLinear(nums):
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
    return max(robLinear(nums[:-1]), robLinear(nums[1:]))
nums = [2,3,2]
print(robCircular(nums))
