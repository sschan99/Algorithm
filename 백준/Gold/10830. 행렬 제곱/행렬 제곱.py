import sys
input = sys.stdin.readline

def matrix_mult(m1, m2):
    n = len(m2)
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m3[i][j] = sum(
                m1[i][k] * m2[k][j]
                for k in range(n)
            ) % 1000
    return m3

def main():
    n, b = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = [[int(i == j) for j in range(n)] for i in range(n)]
    
    while b:
        b, r = divmod(b, 2)
        if r:
            result = matrix_mult(result, matrix)
        matrix = matrix_mult(matrix, matrix)
    
    for row in result:
        print(*row)

if __name__ == '__main__':
    main()