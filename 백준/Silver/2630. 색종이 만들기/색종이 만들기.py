import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

output = [0, 0]

def run(i, j, n):
    color = matrix[i][j]
    for _i in range(i, i + n):
        for _j in range(j, j + n):
            if color != matrix[_i][_j]:
                _n = n // 2
                run(i, j, _n)
                run(i + _n, j, _n)
                run(i, j + _n, _n)
                run(i + _n, j + _n, _n)
                return
    output[color] += 1

run(0, 0, n)
print(output[0])
print(output[1])