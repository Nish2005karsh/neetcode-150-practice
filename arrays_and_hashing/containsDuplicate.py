def containsDuplicate(nums):
    if(len(nums)==len(set(nums))):
        return False
    else:
        return True
nums=[1,2,3,1]
print(containsDuplicate(nums))

#Other method
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if(nums[i]==nums[i+1]):
            return True
        return False
nums=[1,2,3,1]
print(containsDuplicate(nums))

# complexity is O(nlogn)
# Third method using hashmap
def containsDuplicate(nums):
    hashmap={}
    for i in range(len(nums)):
        if(nums[i] in hashmap):
            return True
        else:
            hashmap[nums[i]]=i
    return False
nums=[1,2,3,1]
print(containsDuplicate(nums))