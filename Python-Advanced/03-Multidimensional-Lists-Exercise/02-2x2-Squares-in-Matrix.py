# 02. 2x2 Squares in Matrix

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)

num_sq_matrix = 0

for row in range(rows):
    for col in range(cols):
        if row - 1 >= 0 and col - 1 >= 0:
            if matrix[row][col] == matrix[row][col - 1] and \
                    matrix[row][col] == matrix[row - 1][col] and \
                    matrix[row][col] == matrix[row - 1][col - 1]:
                num_sq_matrix += 1

print(num_sq_matrix)