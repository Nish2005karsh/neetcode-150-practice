def twosum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        if(target-nums[i] in hashmap):
            return [hashmap[target-nums[i]],i]
        hashmap[nums[i]]=i
    return []
nums=[2,7,11,15]
target=9
print(twosum(nums,target))
