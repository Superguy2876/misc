class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min = 0
        max = len(nums) - 1

        while max >= min:
            index = (max + min) // 2

            if nums[index] > target:
                max = index - 1
            elif nums[index] < target:
                min = index + 1
            else:
                return index
        return -1

import random

bs = Solution()
# test cases, lists are sorted

# test case 1
nums = [-1,0,3,5,9,12]
target = 9
print(bs.search(nums, target))

# test case 2
nums = [-1,0,3,5,9,12]
target = 2
print(bs.search(nums, target))

# test case 3
nums = [5]
target = 5
print(bs.search(nums, target))

# test case 4
nums = [5]
target = 2
print(bs.search(nums, target))

# test case 5
nums = [5, 6]
target = 5
print(bs.search(nums, target))

# test case 6
nums = [5, 6]
target = 6
print(bs.search(nums, target))

# test case 7
nums = [5, 6]
target = 2
print(bs.search(nums, target))

# test case 8
nums = [5, 6]
target = 7
print(bs.search(nums, target))

# test case 9, large list
nums = [i for i in range(1000000)]



target = 999999
print(bs.search(nums, target))