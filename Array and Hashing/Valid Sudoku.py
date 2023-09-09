'''
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''

# Using hashset to check each cell
import math 
class Solution:
    def isValidSudoku(  board):
        # Hash-set for columns
        columnDict = {
            0 : set(),
            1 : set(),
            2 : set(),
            3 : set(),
            4 : set(),
            5 : set(),
            6 : set(),
            7 : set(),
            8 : set()
        }
        # Hash-set for square
        squareDict = {
            (0,0) : set(),
            (0,1) : set(),
            (0,2) : set(),
            (1,0) : set(),
            (1,1) : set(),
            (1,2) : set(),
            (2,0) : set(),
            (2,1) : set(),
            (2,2) : set()
        }
        for i in range(len(board)):
            nums = set()
            for j in range(len(board)):
                num = board[i][j]
                if num == '.':
                    continue
                n = (math.floor(i/3), math.floor(j/3))
                if num in nums or num in columnDict[j] or num in squareDict[n]:
                    return False
                nums.add(num)
                columnDict[j].add(num)
                squareDict[n].add(num)
        return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(Solution.isValidSudoku(board))