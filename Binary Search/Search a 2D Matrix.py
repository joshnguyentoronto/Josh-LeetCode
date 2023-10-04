'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

class Solution:
    def searchMatrix(matrix, target):
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row - 1
        selectRow = 0
        while top <= bot:
            mid = (bot + top) // 2
            if target == matrix[mid][0]:
                return True    
            elif target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else: 
                break
        if not (top <= bot):
            return False
        selectRow = (top + bot) // 2
        r, l = 0, col - 1
        while r < l:
            mid = (l + r) // 2
            if target in [matrix[selectRow][r], matrix[selectRow][mid], matrix[selectRow][l]]:
                return True
            elif target < matrix[selectRow][mid]:
                l = mid - 1
            elif target > matrix[selectRow][mid]:
                r = mid + 1
            else:
                return True
        return False

print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print('=========')
print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))