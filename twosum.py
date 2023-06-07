class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstno = 0
        secondno = len(numbers) - 1
        
        # input list is sorted
        # use two pointers, one at the start and one at the end
        # if the second pointer is bigger than the target, move it down
        while numbers[firstno] + numbers[secondno] != target:
            if numbers[firstno] + numbers[secondno] > target:
                secondno -= 1
            else:
                firstno += 1
        return [firstno + 1, secondno + 1]