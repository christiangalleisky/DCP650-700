def has_equal_values(matrix, row, col):
    m, n = len(matrix), len(matrix[0])

    start = matrix[row][col]
    while row < m and col < n:
        if matrix[row][col] != start:
            return False
        row += 1; col += 1

    return True

def is_toeplitz(matrix):
    m, n = len(matrix), len(matrix[0])

    for row in range(m):
        if not has_equal_values(matrix, row, 0):
            return False
    for col in range(1, n):
        if not has_equal_values(matrix, 0, col):
            return False

    return True
