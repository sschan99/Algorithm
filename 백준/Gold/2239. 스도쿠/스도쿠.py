import sys
input = sys.stdin.readline

matrix = [list(map(int, input().strip())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]

def print_matrix():
    for row in matrix:
        print(''.join(map(str, row)))

def check(x, y, num):
    for i in range(9):
        if num in (matrix[x][i], matrix[i][y]):
            return False
    i, j = (x // 3) * 3, (y // 3) * 3
    for k in range(3):
        for l in range(3):
            if num == matrix[i + k][j + l]:
                return False
    return True

def sudoku(n):
    if n == len(zero):
        print_matrix()
        exit()
    x, y = zero[n]
    if matrix[x][y] != 0:
        sudoku(n + 1)
        return
    for num in range(1, 10):
        if check(x, y, num):
            matrix[x][y] = num
            sudoku(n + 1)
            matrix[x][y] = 0

sudoku(0)