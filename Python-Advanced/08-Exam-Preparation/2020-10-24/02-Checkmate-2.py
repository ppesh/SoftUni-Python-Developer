# 02. Checkmate

def right_down_diagonal_queen(r,c):
 
    for i in range(size - r):
        r += 1
        c += 1
        if r  in range(size) and c  in range(size):
            if matrix[r][c] == "Q":
                return [r, c]
 
 
def left_up_diagonal_queen(r, c):
 
    for i in range(size - r):
        r -= 1
        c -= 1
        if r  in range(size) and c  in range(size):
            if matrix[r][c] == "Q":
                return [r, c]
 
 
def right_up_diagonal_queen(r, c):
 
    for i in range(size - r):
        r -= 1
        c += 1
        if r in range(size) and c  in range(size):
            if matrix[r][c] == "Q":
                return [r, c]
 
 
def left_down_diagonal_queen(r, c):
 
    for i in range(size - r):
        r += 1
        c -= 1
        if r in range(size) and c in range(size):
            if matrix[r][c] == "Q":
                return [r, c]
 
 
def left_horizontal_queen(r, c):
 
    for i in range(c, -1, -1):
 
        if matrix[r][i] == "Q":
            return [r, i]
 
def right_horizontal_queen(r, c):
 
    for i in range(c, size):
 
        if matrix[r][i] == "Q":
            return [r, i]
 
 
def up_vertical_queen(r, c):
 
    for i in range(r, -1, -1):
 
        if matrix[i][c] == "Q":
            return [i, c]
 
 
 
def down_vertical_queen(r, c):
 
    for i in range(r, size):
 
        if matrix[i][c] == "Q":
            return [i, c]
 
 
size = 8
 
matrix = []
for chess_deck in range(size):
    row = input().split()
    matrix.append([])
    for el in row:
        matrix[chess_deck].append(el)
 
 
king_coordinates = ()
for i in range(size):
 
    if "K" in matrix[i]:
        king_index = matrix[i].index("K")
        king_coordinates = (i, king_index)
 
king_row = king_coordinates[0]
king_col = king_coordinates[1]
queens = []
 
queens.append(right_down_diagonal_queen(king_row, king_col))
 
queens.append(left_up_diagonal_queen(king_row, king_col))
 
queens.append(right_up_diagonal_queen(king_row, king_col))
 
queens.append(left_down_diagonal_queen(king_row, king_col))
 
queens.append(left_horizontal_queen(king_row, king_col))
 
queens.append(right_horizontal_queen(king_row, king_col))
 
queens.append((up_vertical_queen(king_row,king_col)))
 
queens.append((down_vertical_queen(king_row,king_col)))
 
 
queens = list(filter(lambda a: a!= None, queens))
 
if queens:
    for el in queens:
        print(el)
 
else:
    print("The king is safe!")