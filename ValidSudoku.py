"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:



"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set=defaultdict(set)
        col_set=defaultdict(set)
        grid_set=defaultdict(lambda: defaultdict(set))

        for row in range(len(board[0])):
            for col in range(len(board)):
                value = board[row][col]
                if value ==".":
                    continue
                if value in row_set[row]:
                    return False

                if value in col_set[col]:
                    return False
                
                if value in grid_set[row//3][col//3]:
                    return False
             

                row_set[row].add(value)
                col_set[col].add(value)
                grid_set[row//3][col//3].add(value)


        return True



        