# 03. Problem

def get_magic_triangle(n):
    matrix = []
    for i in range(2):
        matrix.append([])
        matrix[i] += (i + 1) * [1]
    for r in range(2, n):
        matrix.append([])
        for c in range(r + 1):
            if c == 0:
                matrix[r].append(matrix[r - 1][c])
            elif 0 < c < r:
                matrix[r].append(matrix[r - 1][c - 1] + matrix[r - 1][c])
            elif c == r:
                matrix[r].append(matrix[r - 1][c - 1])
    return matrix
	
# Test Code
print(get_magic_triangle(5))

