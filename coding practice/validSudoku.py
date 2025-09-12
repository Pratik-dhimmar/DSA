# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

a = [[".","8",".",".",".",".",".",".","."],[".",".",".",".","2",".",".",".","."],[".","6",".",".",".",".","1",".","4"],[".",".",".","9",".",".","7",".","."],[".",".",".",".",".",".",".","4","."],[".",".","1",".",".","8",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".","5",".","7","."],[".",".","3",".",".","5","6",".","."]]

def format(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if j in [2,5]:
                print(a[i][j], end = "|")
            else:print(a[i][j], end = " ")
        print()
        if i in [2,5]:
            print("-"*20)

def print2d(a):
    for x in a:
        for y in x:
            print(y,end=" ")
        print()
 

def validSudoku(board):
        # # more space less loops
        # row = [set() for _ in range(9)]
        # col = [set() for _ in range(9)]
        # box = [set() for _ in range(9)]

        # for i in range(9):
        #     for j in range(9):
        #         c = (board[i][j])
        #         if c != ".":
        #             boxI = (i//3)*3 + j//3
        #             if c in row[i] or c in col[j] or c in box[boxI]:
        #                 return False
                    
        #             row[i].add(c)
        #             col[j].add(c)
        #             box[boxI].add(c)
        
        # return True 

#more loops less space

    for i in range(9):  #for rows
        set1 = set()
        for j in range(9):
            c = board[i][j]
            if c != ".":
                if c in set1:
                    return False
                else:
                    set1.add(c)
            
    for i in range(9):  #for cols
        set1 = set()
        for j in range(9):
            c = board[j][i]
            if c != ".":
                if c in set1:
                    return False
                else:
                    set1.add(c)

    index = [(0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)]
    for i_start,j_start in index:
        set1 = set()
        for i in range(i_start,i_start+3):
            for j in range(j_start,j_start+3):
                c = board[i][j]
                if c != ".":
                    if c in set1:
                        return False
                    else:
                        set1.add(c)
    return True

print(validSudoku(a))
format(a)