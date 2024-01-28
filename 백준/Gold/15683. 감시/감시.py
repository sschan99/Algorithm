import sys
input = sys.stdin.readline


def copy(matrix):
    return [row[:] for row in matrix]


def set_camera(matrix, start, size, direction):
    i, j = start
    n, m = size
    while 0 <= i < n and 0 <= j < m:
        if matrix[i][j] == 6:
            break
        if matrix[i][j] == 0:
            matrix[i][j] = -1
        i += direction[0]
        j += direction[1]
    return matrix


def cal_result(matrix):
    count = 0
    for row in matrix:
        for elem in row:
            if elem == 0:
                count += 1
    return count


def run(matrix, skip, size):
    s_i, s_j = skip
    n, m = size

    for i in range(s_i, n):
        for j in range(0, m):
            if i == s_i and j <= s_j:
                continue
            
            now = (i, j)
            elem = matrix[i][j]
            if elem == 1:
                copy_matrix = [copy(matrix) for _ in range(4)]
                
                set_camera(copy_matrix[0], now, size, (0, 1))
                set_camera(copy_matrix[1], now, size, (0, -1))
                set_camera(copy_matrix[2], now, size, (1, 0))
                set_camera(copy_matrix[3], now, size, (-1, 0))

                return min(run(c, now, size) for c in copy_matrix)

            elif elem == 2:
                copy_matrix = [copy(matrix) for _ in range(2)]
                
                set_camera(copy_matrix[0], now, size, (0, 1))
                set_camera(copy_matrix[0], now, size, (0, -1))
                set_camera(copy_matrix[1], now, size, (1, 0))
                set_camera(copy_matrix[1], now, size, (-1, 0))

                return min(run(c, now, size) for c in copy_matrix)
                
            elif elem == 3:
                copy_matrix = [copy(matrix) for _ in range(4)]
                
                set_camera(copy_matrix[0], now, size, (0, 1))
                set_camera(copy_matrix[0], now, size, (1, 0))
                set_camera(copy_matrix[1], now, size, (0, 1))
                set_camera(copy_matrix[1], now, size, (-1, 0))
                set_camera(copy_matrix[2], now, size, (0, -1))
                set_camera(copy_matrix[2], now, size, (1, 0))
                set_camera(copy_matrix[3], now, size, (0, -1))
                set_camera(copy_matrix[3], now, size, (-1, 0))

                return min(run(c, now, size) for c in copy_matrix)
            
            elif elem == 4:
                copy_matrix = [copy(matrix) for _ in range(4)]
                
                set_camera(copy_matrix[0], now, size, (0, 1))
                set_camera(copy_matrix[0], now, size, (0, -1))
                set_camera(copy_matrix[0], now, size, (1, 0))
                set_camera(copy_matrix[1], now, size, (0, 1))
                set_camera(copy_matrix[1], now, size, (0, -1))
                set_camera(copy_matrix[1], now, size, (-1, 0))
                set_camera(copy_matrix[2], now, size, (0, 1))
                set_camera(copy_matrix[2], now, size, (1, 0))
                set_camera(copy_matrix[2], now, size, (-1, 0))
                set_camera(copy_matrix[3], now, size, (0, -1))
                set_camera(copy_matrix[3], now, size, (1, 0))
                set_camera(copy_matrix[3], now, size, (-1, 0))

                return min(run(c, now, size) for c in copy_matrix)
            
            elif elem == 5:
                copy_matrix = [copy(matrix) for _ in range(1)]
                
                set_camera(copy_matrix[0], now, size, (0, 1))
                set_camera(copy_matrix[0], now, size, (0, -1))
                set_camera(copy_matrix[0], now, size, (1, 0))
                set_camera(copy_matrix[0], now, size, (-1, 0))

                return min(run(c, now, size) for c in copy_matrix)

    return cal_result(matrix)


def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result = run(matrix, (0, -1), (n, m))
    print(result)
        

if __name__ == '__main__':
    main()