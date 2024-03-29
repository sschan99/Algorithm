import sys
input = sys.stdin.readline

def main():
    matrix = [list(map(int, input().strip())) for _ in range(9)]

    row_cond = []
    for i in range(9):
        cond = set(range(1, 10))
        for j in range(9):
            cond.discard(matrix[i][j])
        row_cond.append(cond)

    col_cond = []
    for i in range(9):
        cond = set(range(1, 10))
        for j in range(9):
            cond.discard(matrix[j][i])
        col_cond.append(cond)

    block_cond = []
    for i in range(3):
        temp = []
        for j in range(3):
            cond = set(range(1, 10))
            for k in range(3):
                for l in range(3):
                    cond.discard(matrix[i * 3 + k][j * 3 + l])
            temp.append(cond)
        block_cond.append(temp)

    def print_matrix():
        for row in matrix:
            print(''.join(map(str, row)))

    def get_next(x, y):
        if y < 8:
            return x, y + 1
        return x + 1, 0

    def sudoku(x, y):
        if x > 8:
            print_matrix()
            exit()
        nx, ny = get_next(x, y)
        if matrix[x][y] != 0:
            sudoku(nx, ny)
            return
        r = row_cond[x].copy()
        c = col_cond[y].copy()
        b = block_cond[x // 3][y // 3].copy()
        for num in sorted(r & c & b):
            matrix[x][y] = num
            if num in r:
                row_cond[x].remove(num)
            if num in c:
                col_cond[y].remove(num)
            if num in b:
                block_cond[x // 3][y // 3].remove(num)
            sudoku(nx, ny)
            if num in r:
                row_cond[x].add(num)
            if num in r:
                col_cond[y].add(num)
            if num in b:
                block_cond[x // 3][y // 3].add(num)
            matrix[x][y] = 0

    sudoku(0, 0)

if __name__ == '__main__':
    main()