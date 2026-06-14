
# Valid Sudoku
# Medium
# Topics
# Company Tags
# Hints
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.


# Brute force solution:


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Visit every cell
        for r in range(9):
            for c in range(9):

                # Skip empty cells
                if board[r][c] == ".":
                    continue

                num = board[r][c]  # Current number to validate

                # Check entire row for duplicates
                for col in range(9):
                    if col != c and board[r][col] == num:
                        return False

                # Check entire column for duplicates
                for row in range(9):
                    if row != r and board[row][c] == num:
                        return False

                # Find top-left corner of current 3x3 box
                startRow = (r // 3) * 3
                startCol = (c // 3) * 3

                # Check all cells in the 3x3 box
                for i in range(startRow, startRow + 3):
                    for j in range(startCol, startCol + 3):

                        # Skip current cell and look for duplicates
                        if (i != r or j != c) and board[i][j] == num:
                            return False

        # No duplicates found
        return True
    
# Brute Force : O(n^3) , Space : O(1)

# The set solution is optimal because we dont have to scan rows, columns, and boxes repeatedly .


# Optimal solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
     cols = collections.defaultdict(set)  # prevents us from key error normally when accessing empty row[0] -> key error
      # if the defaultdic is used then simply returns empty set
     rows = collections.defaultdict(set)
     squares = collections.defaultdict(set)

     for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or    # numbers already seen in row r
                 board[r][c] in cols[c] or     # numbers already seen in column c
                 board[r][c] in squares [(r//3,c//3)]): # numbers already seen in that 3x3 box
               return False
            
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
     return True




     # Time complexity : O(n^2)
     # Space complextiy: O(n^2)





     # The time and space complexity for fixed sudoku solution of 9*9 grid is:
     # Time complexity = O(1)
     # Space complexity = O(1)
     # It is because the size of the grid is fixed 9*9


     # However, if the grid was dynamic ( can grow in size ) then the time and space complexity will differ:

     # For Brute force solution:
       # The Time complexity is O(n^3)

        #   for r in range(n) -> row O(n)
        #      for c in range(n) -> column scan
        #         for grid  check scanning a 3*3 box -> O(n)

        #         Total : O(n^3)

        # Space complexity = O(1) -> no additional space needed

    
    # Using the optimal solution:
        # The time complexity is O(n^2)

        #  for r in range(n) -> row O(n)
        #      for c in range(n) -> column scan

        #      Total : O(n^2)
    
        # # For the space complexity then:
        #    we used dictionary so : 
        #       the space complexity for a row dictionary : 
        #         rows {
        #             0 : {1,2,3,4},
        #             1 : {1,2,3,4},
        #             2: {1,2,3,4},
        #             3: {1,2,3,4}
        #         }
        #         so the space complexity becomes O(n^2) , then likewise for the total space complexity :
        #           n^2 + n^2 + n^2

        #           : How many values are stored : 16 diff values: which is 4^2 i.e n^2
