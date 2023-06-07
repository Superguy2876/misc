class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # first binary search on the first column to find the row
        # then binary search on the row to find the target

        # binary search on the first column
        min = 0
        max = len(matrix) - 1

        while max >= min:
            index = (max + min) // 2

            if matrix[index][0] > target:
                max = index - 1
            elif matrix[index][0] < target:
                min = index + 1
            else:
                return True
        
        # if the target is less than the smallest element in the matrix
        # then it is not in the matrix
        if max < 0:
            return False
        
        # binary search on the row
        min = 0
        max = len(matrix[index]) - 1

        while max >= min:
            index2 = (max + min) // 2

            if matrix[index][index2] > target:
                max = index2 - 1
            elif matrix[index][index2] < target:
                min = index2 + 1
            else:
                return True
            
        return False


tdbs = Solution()

# test case 1
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(tdbs.searchMatrix(matrix, target))