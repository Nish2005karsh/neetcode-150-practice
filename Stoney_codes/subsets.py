def subsets(nums):
    res,sol=[],[]
    def backtracking(i):
        if i==len(nums):
            res.append(sol.copy())
            return
        # decision to not  include nums[i]
        backtracking(i+1)
        # decision to include nums[i]
        sol.append(nums[i])
        backtracking(i+1)
        sol.pop()
    backtracking(0)
    return res
nums=[1,2,3]
print(subsets(nums))

