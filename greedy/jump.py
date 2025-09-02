# Using greedy approach
def canJump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
nums = [2,3,1,1,4]
print(canJump(nums))  # Output: True