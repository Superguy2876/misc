from itertools import combinations

nums = [1,2,3,4]

# this function when given a list of numbers and a number k, returns a list of indices of the combination that sums to k
def combosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return None
    
print(combosum(nums, 5))